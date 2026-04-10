using Mediator;

IAirTrafficControl airTrafficControl=new AirTrafficControl();

var passengerPlane = new PassengerAircraft("PassengerPlan1",airTrafficControl);
var cargoPlan = new CargoAircraft("CargoPlane1",airTrafficControl);

passengerPlane.Send("Requesting Permission to land.");
cargoPlan.Send("Acknowleged, Holding patter");
