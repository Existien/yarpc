// struct MyHandlers{
//     pub pref: String
// }
// #[async_trait]
// impl HandlerTrait for MyHandlers {
//     async fn handle_bump(&self) {
//         println!("nothing");
//         sleep(Duration::from_secs(1)).await;
//         println!("something");
//     }
//     async fn handle_echo(&self, msg: String) -> String {
//         format!("{}: {}",self.pref, msg)
//     }
// }

// #[tokio::main]
// pub async fn main() -> Result<(), Box<dyn std::error::Error>> {
//     let mut client = nogen::minimal::Client::connect().await?;

//     client.on_bumped(|_, ()|{
//         println!("Bumped received!");
//         true
//     }).await?;
//     let iface = nogen::minimal::Interface::connect().await?;
//     let state = Arc::new(RwLock::new(MyHandlers{pref: "Foo".to_string()}));
//     iface.set_handlers(state.clone()).await;
//     let iface_clone = iface.clone();

//     let calls = async move {
//         let c = nogen::minimal::Client::connect().await?;
//         let mut i = 0;
//         loop {
//             i +=1;
//             println!("Call Bump");
//             let x = c.bump().await;
//             iface_clone.emit_bumped();
//             {
//                 let s: String = i.to_string();
//                 (state.write().await).pref = s;
//             }

//             match x {
//                 Ok(_) => {println!("OK");},
//                 Err(e) => {println!("ERR {}",e);},
//             };
//             sleep(Duration::from_secs(2)).await;
//         }

//         #[allow(unreachable_code)]
//         Result::<(), dbus::Error>::Ok(())
//     };

//     tokio::spawn(calls);

//     future::pending::<()>().await;
//     unreachable!()
// }