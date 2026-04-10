namespace Bridge;

public interface IDevice
{
    void TurnOn();
    void TurnOff();
    void SetVolume(int level);

}

public class Tv : IDevice
{
    public void SetVolume(int level)
    {
        Console.WriteLine($"TV volume is on {level}");
    }

    public void TurnOff()
    {
        Console.WriteLine("TV is now off.");
    }

    public void TurnOn()
    {
        Console.WriteLine("TV is now on.");

    }
}

public class Projector : IDevice
{
    public void SetVolume(int level)
    {
        Console.WriteLine($"Projector volume is on {level}");
    }

    public void TurnOff()
    {
        Console.WriteLine("Projector is now off.");
    }

    public void TurnOn()
    {
        Console.WriteLine("Projector is now on.");

    }
}

public class RemoteControl
{
    protected IDevice _device;

    public RemoteControl(IDevice device)
    {
        _device = device;
    }

    public void SetVolume(int level)
    {
        _device.SetVolume(level);
    }

    public void TurnOff()
    {
        _device.TurnOff();
    }

    public void TurnOn()
    {
        _device.TurnOn();

    }

}


