PaymentProcessor processor = new PaymentProcessor();

//Credit card strategy
processor.SetPaymentStrategy(new CreditCardPayment());
processor.ProcessPayment(200);

//paypal strategy
processor.SetPaymentStrategy(new PaypalPayment());
processor.ProcessPayment(100);

  