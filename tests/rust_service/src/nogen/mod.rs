#![allow(dead_code)]
pub mod minimal;

use tokio::task::JoinHandle;
use std::sync::{Arc, LazyLock};
use dbus::nonblock::{SyncConnection};
use dbus_tokio::connection;
use tokio::sync::Mutex;

struct Connection {
    handle: JoinHandle<()>,
    connection: Arc<SyncConnection>,
}

impl Connection {
    pub async fn new() -> Result<Self, dbus::Error> {
        let (resource, connection) = connection::new_session_sync()?;
        let handle = tokio::spawn(async {
            let err = resource.await;
            panic!("Lost connection to D-Bus: {}", err);
        });
        Ok(Self{handle, connection})
    }

    pub fn connect(&self) -> Arc<SyncConnection> {
        self.connection.clone()
    }

    pub fn connection_count(&self) -> usize {
        Arc::<SyncConnection>::strong_count(&self.connection) - 2
    }
}

impl Drop for Connection {
    fn drop(&mut self) {
        self.handle.abort();
    }
}

static CONNECTION: LazyLock<Mutex<Option<Connection>>> = LazyLock::new(||{Mutex::new(None)});

async fn connect() -> Result<Arc<SyncConnection>, dbus::Error> {
    let mut guard = CONNECTION.lock().await;
    if (*guard).is_none() {
        let c = Connection::new().await?;
        *guard = Some(c);
    }
    let cloned_connection = (*guard).as_ref().unwrap().connect();
    Ok(cloned_connection)
}

async fn close() -> Result<(), dbus::Error> {
    let mut guard = CONNECTION.lock().await;
    if (*guard).is_some() {
        let users = (*guard).as_ref().unwrap().connection_count();
        if users == 0  {
            *guard = None;
        } else {
            return Err(dbus::Error::new_failed(&format!("Unable to close. Connection is still used by {} clients.", users)));
        }
    }
    Ok(())
}