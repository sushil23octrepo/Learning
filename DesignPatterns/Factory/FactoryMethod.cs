namespace Factory;


public abstract class PizzaStore
{
    public abstract IPizza CreatePizza();
}

public class VeggiePizzaStore : PizzaStore
{
    public override IPizza CreatePizza()=>new VeggiePizza();
    
}

public class PepperOniPizzaStore : PizzaStore
{
    public override IPizza CreatePizza() => new PepperOniPizza();

}

public class CheesePizzaStore : PizzaStore
{
    public override IPizza CreatePizza() => new PepperOniPizza();

}