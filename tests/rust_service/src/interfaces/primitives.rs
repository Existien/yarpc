use std::sync::Arc;
use async_trait::async_trait;
use tokio::{sync::RwLock};
use super::generated::{PrimitivesInterface, PrimitivesInterfaceHandlers, BackendPrimitivesClient};


pub struct PrimitivesHandlers {}

#[async_trait]
impl PrimitivesInterfaceHandlers for PrimitivesHandlers {
    async fn handle_uint8_method(&self, value: u8, ) -> Result<(u8,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.uint8_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_bool_method(&self, value: bool, ) -> Result<(bool,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.bool_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_int16_method(&self, value: i16, ) -> Result<(i16,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.int16_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_uint16_method(&self, value: u16, ) -> Result<(u16,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.uint16_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_int32_method(&self, value: i32, ) -> Result<(i32,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.int32_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_uint32_method(&self, value: u32, ) -> Result<(u32,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.uint32_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_int64_method(&self, value: i64, ) -> Result<(i64,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.int64_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_uint64_method(&self, value: u64, ) -> Result<(u64,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.uint64_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_double_method(&self, value: f64, ) -> Result<(f64,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.double_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
    async fn handle_string_method(&self, value: String, ) -> Result<(String,) ,dbus::MethodErr> {
        let client = BackendPrimitivesClient::connect().await;
        match &client {
            Ok(c) => {c.string_method(value).await},
            _ => Err(dbus::MethodErr::failed("Failed to forward to client"))
        }
    }
}

pub async fn configure_primitives() -> Result<(PrimitivesInterface, BackendPrimitivesClient),dbus::Error> {
    let state = Arc::new(RwLock::new(PrimitivesHandlers{}));
    let iface = PrimitivesInterface::connect_with_handlers(state.clone()).await?;
    let mut client = BackendPrimitivesClient::connect().await?;
    let iface_clone = iface.clone();
    client.on_uint8_signal(move |_, (value,): (u8,)|{
        iface_clone.emit_uint8_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_bool_signal(move |_, (value,): (bool,)|{
        iface_clone.emit_bool_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_int16_signal(move |_, (value,): (i16,)|{
        iface_clone.emit_int16_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_uint16_signal(move |_, (value,): (u16,)|{
        iface_clone.emit_uint16_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_int32_signal(move |_, (value,): (i32,)|{
        iface_clone.emit_int32_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_uint32_signal(move |_, (value,): (u32,)|{
        iface_clone.emit_uint32_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_int64_signal(move |_, (value,): (i64,)|{
        iface_clone.emit_int64_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_uint64_signal(move |_, (value,): (u64,)|{
        iface_clone.emit_uint64_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_double_signal(move |_, (value,): (f64,)|{
        iface_clone.emit_double_signal(value);
        true
    }).await?;
    let iface_clone = iface.clone();
    client.on_string_signal(move |_, (value,): (String,)|{
        iface_clone.emit_string_signal(value);
        true
    }).await?;
    Ok((iface, client))
}

