from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_venue = models.CharField(max_length=50)
    total_tickets = models.IntegerField()
    

class Sponsor(models.Model):
    sponsor_id = models.IntegerField(primary_key=True)
    sponsor_name = models.CharField(max_length=50)
    sponsor_amount = models.IntegerField()


class EventSponsor(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor_id = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='events')


class Performer(models.Model):
    performer_id = models.IntegerField(primary_key=True)
    performer_name = models.CharField(max_length=50)
    performer_genre = models.CharField(max_length=50)

class EventPerformer(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    performer_id = models.ForeignKey(Performer, on_delete=models.CASCADE, related_name='events')

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    customer_phone = models.BigIntegerField()

class Ticket(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_price = models.IntegerField()


class Club(models.Model):
    club_id = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=50)

class Organizes(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

class Vendor(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    vendor_location = models.CharField(max_length=50)


class EventVendor(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='events')
