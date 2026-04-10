namespace Observer;

public class Newsletter
{
    private readonly List<ISubscriber> _subscribers = new List<ISubscriber>();
    public void Subscribe(ISubscriber subscriber)
    {
        _subscribers.Add(subscriber);
    }

    public void UnSubscribe(ISubscriber subscriber)
    {
        _subscribers.Remove(subscriber);
    }

    public void NotifySubscribers(string content)
    {
        foreach (var subscriber in _subscribers)
        {
            subscriber.Update(content);
        }
    }

}

public interface ISubscriber
{
    void Update(string content);
}

public class EmailSubscriber: ISubscriber
{
    private readonly string _email;

    public EmailSubscriber(string email)
    {
        _email = email;
    }

    public void Update(string content)
    {
        Console.WriteLine($"Email sent to {_email}: {content}");
    }
}

public class SMSSubscriber : ISubscriber
{
    private readonly string _phoneNumber;

    public SMSSubscriber(string phoneNumber)
    {
        _phoneNumber = phoneNumber;
    }

    public void Update(string content)
    {
        Console.WriteLine($"SMS sent to {_phoneNumber}: {content}");
    }
}

