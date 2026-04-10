namespace ProtoType;

public abstract class Shape
{
    public string Color { get; set; }
    public abstract Shape Clone();
}

public class Circle:Shape
{
    public int Radius { get; set; }

    public override Shape Clone()
    {
        return (Shape) this.MemberwiseClone();
    }

    public override string ToString()
    {
        return $"Circle:Radius = {Radius}, Color={Color}";
    }

}

public class Rectangle:Shape
{
    public int Width { get; set; }
    public int Height { get; set; }

    public override Shape Clone()
    {
        return (Shape)this.MemberwiseClone();
    }

    public override string ToString()
    {
        return $"Rectangle: Width= {Width}, Height={Height}, Color={Color}";
    }
}