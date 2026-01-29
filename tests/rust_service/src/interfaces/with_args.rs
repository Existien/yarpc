use std::sync::Arc;
use async_trait::async_trait;
use tokio::{sync::RwLock};
use super::generated::{WithArgsInterface, WithArgsInterfaceHandlers, BackendWithArgsClient};


pub struct WithArgsHandlers {
    speed: f64,
    duration: f64,
    distance: u32,
}

#[async_trait]
impl WithArgsInterfaceHandlers for WithArgsHandlers {
    async fn handle_notify(&self, message: String) -> Result<(), dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {c.notify(message).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_order(&self, item: String, amount: u32, price_per_item: f64) -> Result<(f64,), dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {c.order(item, amount, price_per_item).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn get_speed(&self) -> Result<f64, dbus::MethodErr> {
        Ok(self.speed)
    }
    async fn set_speed(&mut self, value: f64) -> Result<f64, dbus::MethodErr> {
        self.speed = value;
        Ok(self.speed)
    }
    async fn get_distance(&self) -> Result<u32, dbus::MethodErr> {
        Ok(self.distance)
    }
    async fn set_distance(&mut self, value: u32) -> Result<u32, dbus::MethodErr> {
        self.distance = value;
        Ok(self.distance)
    }
    async fn get_duration(&self) -> Result<f64, dbus::MethodErr> {
        Ok(self.duration)
    }
}

pub async fn configure_with_args() -> Result<(WithArgsInterface, BackendWithArgsClient),dbus::Error> {
    let state = Arc::new(RwLock::new(WithArgsHandlers{
        speed:10.0, duration: 20.0, distance: 200
    }));
    let iface = WithArgsInterface::connect_with_handlers(state.clone()).await?;
    let mut client = BackendWithArgsClient::connect().await?;
    let iface_clone = iface.clone();
    client.on_notified(move |_, (message, ): (String,)|{
        println!("SIGNAL RECEIVED");
        iface_clone.emit_notified(message);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_order_received(move |_, (item, amount, price_per_item, ): (String,u32,f64,)|{
        iface_clone.emit_order_received(item, amount, price_per_item);
        true
    }).await?;
    Ok((iface, client))
}

