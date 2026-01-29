use std::sync::Arc;
use async_trait::async_trait;
use tokio::{sync::RwLock};
use super::generated::{MinimalInterface, MinimalInterfaceHandlers, BackendMinimalClient};


pub struct MinimalHandlers {}

#[async_trait]
impl MinimalInterfaceHandlers for MinimalHandlers {
    async fn handle_bump(&self) -> Result<(),dbus::MethodErr> {
        let client = BackendMinimalClient::connect().await;
        match &client {
            Ok(c) => {c.bump().await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }

    }
}

pub async fn configure_minimal() -> Result<(MinimalInterface, BackendMinimalClient),dbus::Error> {
    let state = Arc::new(RwLock::new(MinimalHandlers{}));
    let iface = MinimalInterface::connect_with_handlers(state.clone()).await?;
    let iface_clone = iface.clone();
    let mut client = BackendMinimalClient::connect().await?;
    client.on_bumped(move |_, ()|{
        iface_clone.emit_bumped();
        true
    }).await?;
    Ok((iface, client))
}

