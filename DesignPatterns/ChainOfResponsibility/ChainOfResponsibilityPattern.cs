namespace ChainOfResponsibility;

public abstract class SupportHandler
{
    protected SupportHandler? NextHandler;
    public void SetNextHandler(SupportHandler nextHandler)
    {
        this.NextHandler = nextHandler; 
    }
    public abstract void HandleRequest(string issue);
}

public class BasicSupport: SupportHandler
{
    public override void HandleRequest(string issue)
    {
        if(issue=="Basic")
        {
            Console.WriteLine("Basic Support: Issue resolved at level 1.");
        }
        else
        {
            Console.WriteLine("Basic Support: Escalitng to level 2.");
            NextHandler?.HandleRequest(issue);
        }
    }
}

public class TechnicalSupport : SupportHandler
{
    public override void HandleRequest(string issue)
    {
        if (issue == "Technical")
        {
            Console.WriteLine("Technical Support: Issue resolved at level 2.");
        }
        else
        {
            Console.WriteLine("Basic Support: Escalitng to level 3.");
            NextHandler?.HandleRequest(issue);
        }
    }
}

public class ManagerSupport : SupportHandler
{
    public override void HandleRequest(string issue)
    {
        Console.WriteLine("Manager Support: Issue resolved at level 3.");
    }
}