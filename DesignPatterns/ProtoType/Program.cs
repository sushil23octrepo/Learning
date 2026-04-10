using ProtoType;

Circle originalCircle = new Circle { Color = "Red", Radius = 20 };
Rectangle orginalRectangle=new Rectangle { Color="Blue", Height=15, Width=20 };

Circle clonedCircle=(Circle)originalCircle.Clone();
Rectangle clonedRectangle = (Rectangle)orginalRectangle.Clone();

Console.WriteLine(clonedCircle);
Console.WriteLine(clonedRectangle);