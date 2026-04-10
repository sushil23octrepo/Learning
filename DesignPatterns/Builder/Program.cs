using Builder;

//Builder Pattern client
ICardBuilder builder=new SportsCarBuilder();
CarDirector director=new CarDirector(builder);
director.ConstructSportCar();
Car car= builder.GetResult();
Console.WriteLine(car);

//Fluent Pattern Client

var car1=new FluentCarBuilder().SetEngine("Electric").SetWheels(4).SetBody("Sedan").Build();
Console.WriteLine(car1);