using ChainOfResponsibility;

var basicSupport = new BasicSupport();
var technicalSupport=new TechnicalSupport();
var managerSupport=new ManagerSupport();

basicSupport.SetNextHandler(technicalSupport);
technicalSupport.SetNextHandler(managerSupport);

Console.WriteLine("==Customer Issue: Basic Issue==");
basicSupport.HandleRequest("Basic");

Console.WriteLine("==Customer Issue: Basic Issue==");
basicSupport.HandleRequest("Technical");

Console.WriteLine("==Customer Issue: Escalated==");
basicSupport.HandleRequest("Escalated");