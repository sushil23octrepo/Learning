public interface IPaymentStrategy
{
    void Pay(double amount);
}

public class CreditCardPayment : IPaymentStrategy
{
    public void Pay(double amount)
    {
        Console.WriteLine($"Processing {amount} using credit card");
    }
}

public class PaypalPayment : IPaymentStrategy
{
    public void Pay(double amount)
    {
        Console.WriteLine($"Processing {amount} using Paypal");
    }
}

public class GooglePayPayment : IPaymentStrategy
{
    public void Pay(double amount)
    {
        Console.WriteLine($"Processing {amount} using google pay");
    }
}

public class PaymentProcessor
{
    private IPaymentStrategy? _paymentStrategy;

    public void SetPaymentStrategy(IPaymentStrategy paymentStrategy)
    {
        _paymentStrategy = paymentStrategy;
    }

    public void ProcessPayment(double amount)
    {
        if (_paymentStrategy == null)
        {
            throw new Exception("Payment strategy is not set");
        }

        _paymentStrategy.Pay(amount);
    }
}

