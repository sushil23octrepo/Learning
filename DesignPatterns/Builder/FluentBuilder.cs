namespace Builder;

public class FluentCarBuilder
{
    public Car _car=new Car();

    public FluentCarBuilder SetEngine(string engine)
    {
        _car.Engine= engine;
        return this;
    }
    public FluentCarBuilder SetWheels(int wheels)
    {
        _car.Wheels = wheels;
        return this;
    }
    public FluentCarBuilder SetBody(string body)
    {
        _car.Body = body;
        return this;
    }

    public Car Build()=>_car;
}