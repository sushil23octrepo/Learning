using Decorator;

//Start with simple coffee
ICoffee coffee = new SimpleCoffee();
Console.WriteLine($"{coffee.GetDesription()} Costs {coffee.GetCost()}");

//Add Milk
coffee=new MilkDecorator(coffee);
Console.WriteLine($"{coffee.GetDesription()} Costs {coffee.GetCost()}");


//Add Sugar
coffee =new SugarDecorator(coffee);
Console.WriteLine($"{coffee.GetDesription()} Costs {coffee.GetCost()}");


