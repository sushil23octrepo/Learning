using Proxy;

BankAmount account = new BankAmount(1000);
ATMProxy proxy = new ATMProxy(account);

proxy.Deposit(200);
proxy.Withdraw(100);

if(proxy.Authenticate("123456","123"))
{
    proxy.Deposit(200);
    proxy.Withdraw(100);
    Console.WriteLine($"Current Balance: {proxy.GetBalance()}");
}
