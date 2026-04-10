using Adaptor;

IPaymentProcessor paypalAdaptor=new PayPalAdaptor(new PaypalPayment());
paypalAdaptor.ProcessPayment(100.50m);


IPaymentProcessor stripeAdaptor = new StripeAdaptor(new StripePayment());
stripeAdaptor.ProcessPayment(250.50m);