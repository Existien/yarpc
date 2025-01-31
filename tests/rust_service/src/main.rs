use std::time::Duration;
use tokio::time::sleep;
mod nogen;

#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = nogen::minimal::Client::connect().await?;

    client.on_bumped(|_, ()|{
        println!("Bumped received!");
        true
    }).await?;

    let calls = async {
        let c = nogen::minimal::Client::connect().await?;
        loop {
            println!("Call Bump");
            let x = c.bump().await;
            match x {
                Ok(_) => {println!("OK");},
                Err(e) => {println!("ERR {}",e);},
            };
            sleep(Duration::from_secs(2)).await;
        }

        #[allow(unreachable_code)]
        Result::<(), dbus::Error>::Ok(())
    };

    tokio::spawn(calls);
    sleep(Duration::from_secs(5)).await;

    client.close().await?;
    Ok(())
}

