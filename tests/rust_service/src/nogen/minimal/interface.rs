use std::sync::Arc;
use async_trait::async_trait;
use dbus::nonblock::{SyncConnection};
use dbus_crossroads::Crossroads;
use tokio::sync::{RwLock};
use dbus::channel::{MatchingReceiver, Sender};
use dbus::message::MatchRule;
use dbus::{Message};
use super::super::{connect};

#[async_trait]
pub trait HandlerTrait: Sync+Send {
    async fn handle_bump(&self);
    async fn handle_echo(&self, msg: String) -> String;
}
type SharedOptionalHandlers = Arc<RwLock<Option<Arc<RwLock<dyn HandlerTrait>>>>>;

pub struct Interface{
    connection: Option<Arc<SyncConnection>>,
    handlers: SharedOptionalHandlers,
}

impl Clone for Interface {
    fn clone(&self) -> Interface {
        Interface{connection: self.connection.clone(), handlers: self.handlers.clone()}
    }
}

impl Interface {
    pub async fn set_handlers(&self, handlers: Arc<RwLock<dyn HandlerTrait>>) {
        *(self.handlers.write().await) = Some(handlers);
    }

    pub async fn connect() -> Result<Self, dbus::Error> {
        let mut xr = Crossroads::new();
        let connection = connect().await?;

        let x = Self{
            connection: Some(connection.clone()),
            handlers: Arc::new(RwLock::new(None))
        };

        // Enable async support for xr instance
        xr.set_async_support(Some((connection.clone(), Box::new(|x| {tokio::spawn(x);}))));
        let iface_token = xr.register("com.example.rusttest", |b| {
            // advertise signal in introspection
            b.signal::<(String,), _>("HelloHappened", ("sender",));
            b.signal::<(), _>("Bumped", ());

            b.method_with_cr_async("Bump", (), (), |mut ctx, xr, ()| {
                let handlers: &mut SharedOptionalHandlers = xr.data_mut(ctx.path()).unwrap();
                let cloned_handlers = handlers.clone();
                async move {
                    let optional_handlers = cloned_handlers.read().await;
                    match optional_handlers.as_ref() {
                        Some(h) => {
                            let unlocked_handlers = h.read().await;
                            ctx.reply(Ok(unlocked_handlers.handle_bump().await))
                        },
                        None => ctx.reply(Err(dbus::MethodErr::failed("Not implemented")))
                    }
                }
            });
            b.method_with_cr_async("Echo", ("msg",), ("reply",), |mut ctx, xr, (msg,): (String,)| {
                let handlers: &mut SharedOptionalHandlers = xr.data_mut(ctx.path()).unwrap();
                let cloned_handlers = handlers.clone();
                async move {
                    let optional_handlers = cloned_handlers.read().await;
                    match optional_handlers.as_ref() {
                        Some(h) => {
                            let unlocked_handlers = h.read().await;
                            let reply = unlocked_handlers.handle_echo(msg).await;
                            ctx.reply(Ok((reply,)))
                        },
                        None => ctx.reply(Err(dbus::MethodErr::failed("Not implemented")))
                    }

                }
            });
        });

        xr.insert("/bump", &[iface_token], x.handlers.clone());
        connection.start_receive(MatchRule::new_method_call(), Box::new(move |msg, conn| {
            xr.handle_message(msg, conn).unwrap();
            true
        }));

        connection.request_name("com.example.rusttest", false, true, false).await?;
        Ok(x)
    }

    pub fn emit_bumped(&self) {
        let signal = Message::signal(&"/hello".into(), &"com.example.rusttest".into(), &"Bumped".into());
        if self.connection.is_some() {
            let _ = self.connection.as_ref().unwrap().send(signal);
        }
    }
}