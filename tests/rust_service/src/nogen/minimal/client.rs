use std::sync::Arc;
use dbus::nonblock::{SyncConnection, MsgMatch, Proxy};
use dbus::message::{Message, MatchRule};
use dbus::arg::ReadAll;

use super::super::{connect, close};

pub struct Client {
    connection: Option<Arc<SyncConnection>>,
    signals_handlers: Vec<MsgMatch>,
}
impl Client {
    
    pub async fn connect() -> Result<Self, dbus::Error> {
        let connection = connect().await?;
        let signals_handlers: Vec<MsgMatch> = Vec::new();
        Ok(Self{connection: Some(connection), signals_handlers})
    }

    pub async fn bump(&self) -> Result<(), dbus::Error> {
        match &self.connection {
            Some(c) => {
                let proxy = Proxy::new("com.yarpc.backend", "/com/yarpc/backend/minimal", std::time::Duration::from_secs(5), c.clone());
                proxy.method_call::<(), _, _, _>("com.yarpc.backend.minimal", "Bump", ()).await
            },
            None => Err(dbus::Error::new_failed("Client not connected to D-Bus")),
        }
    }

    pub async fn on_bumped<R: ReadAll, F: FnMut(Message, R) -> bool + Send + 'static>(&mut self, f: F) -> Result<(), dbus::Error> {
        match &self.connection {
            Some(c) => {
                let mr = MatchRule::new_signal("com.yarpc.backend.minimal", "Bumped");
                let signal_matcher = c.add_match(mr).await?.cb(f);
                self.signals_handlers.push(signal_matcher);
                Ok(())
            },
            None => Err(dbus::Error::new_failed("Client not connected to D-Bus")),
        }
    }

    pub async fn close(&mut self) -> Result<(), dbus::Error> {
        if self.connection.is_some() {
            for s in &self.signals_handlers {
                self.connection.as_ref().unwrap().remove_match(s.token()).await?;
            }
        }
        self.connection = None;
        let _ = close().await;
        Ok(())
    }
}