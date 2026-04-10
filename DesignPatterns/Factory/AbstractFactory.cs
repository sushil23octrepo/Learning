namespace Factory;

public interface IStorage
{
    void Upload(string fileName);
}

public interface IQueue
{
    void Send(string message);
}

public interface ICloudFactory
{
    IStorage CreateStorage();
    IQueue CreateQueue();
}

public class AwsStorage() : IStorage
{
    public void Upload(string fileName)
    {
        Console.WriteLine($"Uploading {fileName} to AWS S3");
    }
}

public class AwsQueue : IQueue
{
    public void Send(string message)
    {
        Console.WriteLine($"Sending message to AWS SQS: {message}");
    }
}

public class AwsFactory : ICloudFactory
{
    public IQueue CreateQueue()=> new AwsQueue();
    public IStorage CreateStorage()=>new AwsStorage();
   
}

public class AzureStorage() : IStorage
{
    public void Upload(string fileName)
    {
        Console.WriteLine($"Uploading {fileName} to Azure blob");
    }
}

public class AzureQueue : IQueue
{
    public void Send(string message)
    {
        Console.WriteLine($"Sending message to Azure Service Bus: {message}");
    }
}

public class AzureFactory : ICloudFactory
{
    public IQueue CreateQueue()=> new AzureQueue();
    public IStorage CreateStorage()=>new AzureStorage();
   
}

public class CloudService
{
    private readonly IStorage _storage;
    private readonly IQueue _queue;

    public CloudService(ICloudFactory cloudFactory)
    {
        _storage = cloudFactory.CreateStorage();
        _queue=cloudFactory.CreateQueue();
    }

    public void Process()
    {
        _storage.Upload("file.txt");
        _queue.Send("File uploaded.");
    }

}
