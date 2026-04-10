using Observer;

var newsLetter=new Newsletter();

var emailSubscriber = new EmailSubscriber("test@gmail.com");
var smsSubscriber = new SMSSubscriber("9871301547");

newsLetter.Subscribe(emailSubscriber);
newsLetter.Subscribe(smsSubscriber);

newsLetter.NotifySubscribers("Test content");

newsLetter.UnSubscribe(emailSubscriber);
newsLetter.NotifySubscribers("Test content1");

