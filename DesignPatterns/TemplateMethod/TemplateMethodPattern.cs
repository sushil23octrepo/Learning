namespace TemplateMethod;

public abstract class Beverage
{
    public void PrepareBeverage()
    {
        BoilWater();
        Brew();
        PourInCup();
        AddCondiments();        
    }
    private void BoilWater()
    {
        Console.WriteLine("Boiling water");
    }

    private void PourInCup()
    {
        Console.WriteLine("Pouring into cup.");
    }

    protected abstract void Brew();
    protected abstract void AddCondiments();

}

public class Tea : Beverage
{
    protected override void AddCondiments()
    {
        Console.WriteLine("Adding lemon");
    }

    protected override void Brew()
    {
        Console.WriteLine("Steeping the tea");
    }
}

public class Coffee : Beverage
{
    protected override void AddCondiments()
    {
        Console.WriteLine("Adding sugar and milk.");
    }

    protected override void Brew()
    {
        Console.WriteLine("Dipping coffee through filter.");
    }
}
