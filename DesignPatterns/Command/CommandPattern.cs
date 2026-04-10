namespace Command;

public interface IOrderCommand
{
    void Execute();
    void Undo();
}

public class OrderService 
{
    public void PlaceOrder()
    {
        Console.WriteLine("Order placed");
    }

    public void CancelOrder()
    {
        Console.WriteLine("Order cancelled");
    }

    public void RefundOrder()
    {
        Console.WriteLine("Order refunded");
    }
}

public class PlaceOrderCommand : IOrderCommand
{
    private readonly OrderService _service;

    public PlaceOrderCommand(OrderService service)
    {
        _service = service;
    }

    public void Execute()
    {
        _service.PlaceOrder();
    }

    public void Undo()
    {
        _service.CancelOrder();
    }
}

public class CancelOrderCommand : IOrderCommand
{
    private readonly OrderService _service;

    public CancelOrderCommand(OrderService service)
    {
        _service = service;
    }

    public void Execute()
    {
        _service.CancelOrder();
    }

    public void Undo()
    {
        _service.PlaceOrder();
    }
}


public class OrderInvoker
{
    private readonly Stack<IOrderCommand> _history = new();

    public void ExecuteCommand(IOrderCommand command)
    {
        command.Execute();
        _history.Push(command);
    }

    public void Undo()
    {
        if (_history.Count > 0)
        {
            var command = _history.Pop();
            command.Undo();
        }
    }
}

