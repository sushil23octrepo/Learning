using Bridge;

IDevice tv=new Tv();
RemoteControl tvRemote=new RemoteControl(tv);
tvRemote.TurnOn();
tvRemote.TurnOff();
tvRemote.SetVolume(10);
Console.WriteLine();

IDevice prejector = new Projector();
RemoteControl projectRemote= new RemoteControl(prejector);
projectRemote.TurnOn();
projectRemote.TurnOff();
projectRemote.SetVolume(10);