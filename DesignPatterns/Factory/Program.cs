
using Factory;

////===Simple Factory client===
//Console.WriteLine("Enter pizza type veggie,pepperoni,cheese");
//string? type=Console.ReadLine();

//try
//{
//    IPizza pizza = PizzaFactory.CreatePizza(type ?? "");
//    pizza.Prepare();
//}d
//catch (Exception ex)
//{
//    Console.WriteLine(ex.ToString());
//}

//===Factory Method Client==

PizzaStore store = new VeggiePizzaStore();
IPizza pizza = store.CreatePizza();
pizza.Prepare();

//Abstract Factory client:
ICloudFactory factory = new AwsFactory();
// ICloudFactory factory = new AzureFactory();

var service=new CloudService(factory);
service.Process();