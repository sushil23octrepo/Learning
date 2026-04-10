namespace Decorator;

public interface ICoffee
{
    string GetDesription();
    double GetCost();
}

public class SimpleCoffee : ICoffee
{
    public double GetCost()
    {
        return 0.5;
    }

    public string GetDesription()
    {
        return "Simple Coffee";
    }
}

public abstract class CoffeeDecorator : ICoffee
{
    protected ICoffee _coffee;

    public CoffeeDecorator(ICoffee coffee)
    {
        this._coffee = coffee;
    }
    public virtual double GetCost()
    {
      return  _coffee.GetCost();
    }

    public virtual string GetDesription()
    {
        return _coffee.GetDesription();
    }
}

public class MilkDecorator : CoffeeDecorator
{
    public MilkDecorator(ICoffee coffee):base(coffee)   {}

    public override string GetDesription()
    {
        return base.GetDesription() + ", Milk";
    }

    public override double GetCost()
    {
        return base.GetCost() + 1.5;
    }

}


public class SugarDecorator:CoffeeDecorator
{
    public SugarDecorator(ICoffee coffee):base (coffee) {}

    public override string GetDesription()
    {
        return base.GetDesription() + ", Sugar";
    }

    public override double GetCost()
    {
        return base.GetCost() + 0.5;
    }
}



