namespace Proxy;

public interface IBankAccount
{
    void Deposit(decimal amount);
    void Withdraw(decimal amount);
    decimal GetBalance();
}

public class BankAmount : IBankAccount
{
    private decimal _balance;

    public BankAmount(decimal initialAmount)
    {
        _balance = initialAmount;
    }
    public void Deposit(decimal amount)
    {
        _balance += amount;
        Console.WriteLine($"Deposited: {amount}. Current Balance: {_balance} ");
    }

    public decimal GetBalance()
    {
        return _balance;
    }

    public void Withdraw(decimal amount)
    {
        if (amount > _balance)
        {
            Console.WriteLine("Insufficient funds!");
        }
        else
        {
            _balance -= amount;
            Console.WriteLine($"Withdrew: {amount}. Current Balance: {_balance}");
        }
    }
}

public class ATMProxy : IBankAccount
{
    private readonly BankAmount _realBankAmount;
    public bool _isAuthenticated;

    public ATMProxy(BankAmount realBankAmount)
    {
        _realBankAmount = realBankAmount;
    }

    public bool Authenticate(string cardNumer,string pin)
    {
        _isAuthenticated = cardNumer == "123456" && pin == "123";
        return _isAuthenticated;        
    }

    public void Deposit(decimal amount)
    {
        if (_isAuthenticated)
        {
            _realBankAmount.Deposit(amount);
        }
        else
        {
            Console.WriteLine("Please authenticate first");
        }
    }

    public decimal GetBalance()
    {
        if (_isAuthenticated)
        {
            return _realBankAmount.GetBalance();
        }
        else
        {
            Console.WriteLine("Please authenticate first");
            return 0;
        }
    }

    public void Withdraw(decimal amount)
    {
        if (_isAuthenticated)
        {
            _realBankAmount.Withdraw(amount);
        }
        else
        {
            Console.WriteLine("Please authenticate first");
        }
    }
}
