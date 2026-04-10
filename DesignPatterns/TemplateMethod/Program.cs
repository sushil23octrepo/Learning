using TemplateMethod;

Console.WriteLine("Preparing tea");
Beverage tea = new Tea();
tea.PrepareBeverage();


Console.WriteLine("Preparing Coffee");
Beverage coffee = new Coffee();
coffee.PrepareBeverage();