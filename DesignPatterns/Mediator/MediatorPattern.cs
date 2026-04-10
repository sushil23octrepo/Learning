
namespace Mediator;

public interface IAirTrafficControl
{
    void RegisterAircraft(Aircraft aircraft);
    void SendMessage(string message, Aircraft sender);
}

public class AirTrafficControl : IAirTrafficControl
{
    private readonly List<Aircraft> _aircrafts = new List<Aircraft>();
    public void RegisterAircraft(Aircraft aircraft)
    {
        _aircrafts.Add(aircraft);
    }

    public void SendMessage(string message, Aircraft sender)
    {
        foreach(var airCraft in _aircrafts)
        {
            if(airCraft !=sender)
            {
                airCraft.RecieveMessage(message);
            }

        }
    }
}

public abstract class Aircraft
{
    protected IAirTrafficControl _airTrafficConrol;
    public string Identifier { get; }

    protected Aircraft(string identifier, IAirTrafficControl airTrafficConrol)
    {
        Identifier = identifier;
        _airTrafficConrol = airTrafficConrol;
        _airTrafficConrol.RegisterAircraft(this);
    }

    public void Send(string message)
    {
        Console.WriteLine($"{Identifier} sends message: {message}");
        _airTrafficConrol.SendMessage(message, this);
    }

    public abstract void RecieveMessage (string message);
}

public class PassengerAircraft : Aircraft
{
    public PassengerAircraft(string identifier, IAirTrafficControl airTrafficConrol):base(identifier,airTrafficConrol)
    {    }

    public override void RecieveMessage(string message)
    {
        Console.WriteLine($"{Identifier} received message {message}");
    }
}

public class CargoAircraft : Aircraft
{
    public CargoAircraft(string identifier, IAirTrafficControl airTrafficConrol) : base(identifier, airTrafficConrol)
    { }

    public override void RecieveMessage(string message)
    {
        Console.WriteLine($"{Identifier} received message {message}");
    }
}