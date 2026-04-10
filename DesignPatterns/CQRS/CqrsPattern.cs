namespace CQRS;

public class RoomBooking
{
    public int Id { get; set; }
    public string GuestName { get; set; }
    public DateTime CheckInDate { get; set; }
    public DateTime CheckOutDate { get; set; }
}

public class RoomAvailability
{
    public int RoomId { get; set; }
    public bool IsAvailable { get; set; }
}

public class BookRoomCommand
{
    public string GuestName { get; set; }
    public DateTime CheckInDate { get; set; }
    public DateTime CheckOutDate { get; set; }
}

public class RoomBookingHandler
{
    private List<RoomBooking> _bookings =new List<RoomBooking>();

    public void Handle(BookRoomCommand command)
    {
        var booking = new RoomBooking
        {
            Id = _bookings.Count + 1,
            GuestName = command.GuestName,
            CheckInDate = command.CheckInDate,
            CheckOutDate = command.CheckOutDate,
        };

        _bookings.Add(booking);
    }

}