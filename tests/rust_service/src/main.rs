use futures::future;
mod interfaces;
use interfaces::{configure_minimal, configure_with_args, start_receive};


#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (_min_i,_min_c) = configure_minimal().await?;
    let (_wa_i, _wa_c) = configure_with_args().await?;
    start_receive().await?;
    future::pending::<()>().await;
    unreachable!()
}

