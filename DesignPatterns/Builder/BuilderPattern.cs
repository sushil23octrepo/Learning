namespace Builder;

public class Car
{
    public string Engine { get; set; }
    public int Wheels { get; set; }
    public string Body { get; set; }

    public override string ToString()
    {
        return $"Car with {Engine} engine, {Wheels}, and {Body} body";
    }

}

public interface ICardBuilder
{
    void SetEngine(string engine);
    void SetWheels(int wheels);
    void SetBody(string body);
    Car GetResult();
}

public class SportsCarBuilder : ICardBuilder
{
    private Car _car=new Car();
    public Car GetResult()=> _car;
    public void SetBody(string body)=>_car.Body = body;
    public void SetEngine(string engine)=>_car.Engine = engine;
    public void SetWheels(int wheels)=>_car.Wheels = wheels;
    
}

public class CarDirector
{
    public ICardBuilder _builder;

    public CarDirector(ICardBuilder builder)
    {
        _builder = builder;
    }

    public void ConstructSportCar()
    {
        _builder.SetEngine("V8");
        _builder.SetWheels(4);
        _builder.SetBody("Coupe");
    }
}