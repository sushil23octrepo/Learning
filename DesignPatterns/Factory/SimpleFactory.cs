namespace Factory;

public interface IPizza
{
    void Prepare();
}

public class VeggiePizza : IPizza
{
    public void Prepare()
    {
        Console.WriteLine("Preparing Veggie Pizza.");
    }
}

public class PepperOniPizza : IPizza
{
    public void Prepare()
    {
        Console.WriteLine("Preparing PepperOni Pizza.");
    }
}

public class CheesePizza : IPizza
{
    public void Prepare()
    {
        Console.WriteLine("Preparing Cheese Pizza.");
    }
}

public class PizzaFactory
{
    public static IPizza CreatePizza(string pizzaType)
    {
        return pizzaType.ToLower() switch
        {
            "veggie" => new VeggiePizza(),
            "pepperoni" => new PepperOniPizza(),
            "cheese" => new CheesePizza(),
            _ => throw new ArgumentException("Invalid Pizza type")
        };
    }
}