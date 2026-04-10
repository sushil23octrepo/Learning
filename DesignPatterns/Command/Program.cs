using Command;

var service=new OrderService();
var invoker = new OrderInvoker();

var placeCommand = new PlaceOrderCommand(service);
var cancelCommand = new CancelOrderCommand(service);

invoker.ExecuteCommand(placeCommand);
invoker.ExecuteCommand(cancelCommand);

Console.WriteLine("Undo last action:");
invoker.Undo();