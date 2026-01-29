use std::sync::Arc;
use async_trait::async_trait;
use tokio::{sync::RwLock};
use super::generated::{WithArgsInterface, WithArgsInterfaceHandlers, BackendWithArgsClient, WithArgsInterfaceProperties, BackendWithArgsClientProperties};


pub struct WithArgsHandlers {}

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
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {
                let result = c.get_speed().await;
                match result {
                    Ok(Some(r)) => {Ok(r)},
                    _ => Err(dbus::MethodErr::failed("Failed to retrieve value"))
                }
            },
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }

    async fn get_duration(&self) -> Result<f64, dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {
                let result = c.get_duration().await;
                match result {
                    Ok(Some(r)) => {Ok(r)},
                    _ => Err(dbus::MethodErr::failed("Failed to retrieve value"))
                }
            },
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }

    async fn get_distance(&self) -> Result<u32, dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {
                let result = c.get_distance().await;
                match result {
                    Ok(Some(r)) => {Ok(r)},
                    _ => Err(dbus::MethodErr::failed("Failed to retrieve value"))
                }
            },
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }

    async fn set_speed(&mut self, value: f64) ->  Result<WithArgsInterfaceProperties, dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {
                c.set_speed(value).await?;
                Ok(WithArgsInterfaceProperties{speed: Some(value), ..Default::default() })  
            },
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        } 
    }

    async fn set_distance(&mut self, value: u32) ->  Result<WithArgsInterfaceProperties, dbus::MethodErr> {
        let client = BackendWithArgsClient::connect().await;
        match &client {
            Ok(c) => {
                c.set_distance(value).await?;
                Ok(WithArgsInterfaceProperties{distance: Some(value), ..Default::default() })
            },
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        } 
    }
}

pub async fn configure_with_args() -> Result<(WithArgsInterface, BackendWithArgsClient),dbus::Error> {
    let state = Arc::new(RwLock::new(WithArgsHandlers{}));
    let iface = WithArgsInterface::connect_with_handlers(state.clone()).await?;
    let mut client = BackendWithArgsClient::connect().await?;
    let iface_clone = iface.clone();
    client.on_notified(move |_, (message, ): (String,)|{
        iface_clone.emit_notified(message);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_order_received(move |_, (item, amount, price_per_item, ): (String,u32,f64,)|{
        iface_clone.emit_order_received(item, amount, price_per_item);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_properties_changed(move |_, props: BackendWithArgsClientProperties|{
        tokio::spawn((async move |iface:  WithArgsInterface| {
            let args = props;
            let _ = iface.emit_properties_changed(WithArgsInterfaceProperties{speed: args.speed, distance: args.distance, duration: args.duration}).await;
        })(iface_clone.clone()));
        true
    }).await?;
    Ok((iface, client))
}

