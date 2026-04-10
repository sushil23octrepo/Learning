namespace Adaptor;

public interface IPaymentProcessor
{
    void ProcessPayment(decimal amount);
}

public class PaypalPayment
{
    public void PayUsingPayPal(decimal amount)
    {
        Console.WriteLine($"Payment of {amount} processed via PayPal.");
    }
}

public class StripePayment
{
    public void MakeStripePayment(decimal amount)
    {
        Console.WriteLine($"Payment of {amount} processed via stripe.");
    }
}

public class PayPalAdaptor : IPaymentProcessor
{
    public readonly PaypalPayment _paypalPayment;

    public PayPalAdaptor(PaypalPayment paypalPayment)
    {
        _paypalPayment = paypalPayment;
    }
    public void ProcessPayment(decimal amount)
    {
        _paypalPayment.PayUsingPayPal(amount);
    }
}


public class StripeAdaptor : IPaymentProcessor
{
    public readonly StripePayment _stripePayment;

    public StripeAdaptor(StripePayment stripePayment)
    {
        _stripePayment = stripePayment;
    }
    public void ProcessPayment(decimal amount)
    {
        _stripePayment.MakeStripePayment(amount);
    }
}
