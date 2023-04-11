from django.shortcuts import render, redirect
from .models import Event, Sponsor, EventSponsor, Performer, EventPerformer, Customer, Ticket, Club, Organizes, Vendor, EventVendor

# Create your views here.

def index(request):
    return render(request, 'index.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def addEvents(request):
    if request.method == 'POST':
        #generate event_id
        event_id = Event.objects.count() + 1
        event_name = request.POST['event_name']
        event_date = request.POST['event_date']
        event_time = request.POST['event_time']
        event_venue = request.POST['event_venue']
        total_tickets = request.POST['total_tickets']
        event = Event(event_id=event_id, event_name=event_name, event_date=event_date, event_time=event_time, event_venue=event_venue, total_tickets=total_tickets)
        event.save()
        return render(request, 'addEvents.html', {'message': 'Event added successfully!'})
    return render(request, 'addEvents.html')

def buy_tickets(request):
    if request.method == 'POST':
        customer_email = request.POST['customer_email']
        if not Customer.objects.filter(customer_email=customer_email).exists():
            return render(request, 'buy_tickets.html', {'message': 'Customer does not exist!'})
        customer = Customer.objects.get(customer_email=customer_email)
        event_name = request.POST['event_name']
        event = Event.objects.get(event_name=event_name)
        event.total_tickets -= 1
        if event.total_tickets < 0:
            return render(request, 'buy_tickets.html', {'message': 'Tickets sold out!'})
        else:
            event.save()
            ticket_price = request.POST['ticket_price']
            if Ticket.objects.filter(customer_id=customer, event_id=event).exists():
                return render(request, 'buy_tickets.html', {'message': 'Ticket already bought!'})
            ticket = Ticket(customer_id=customer, event_id=event, ticket_price=ticket_price)
            ticket.save()
            return render(request, 'buy_tickets.html', {'message': 'Ticket bought successfully!', 'events': Event.objects.all()})
    events = Event.objects.all()
    return render(request, 'buy_tickets.html', {'events': events})


def create_customer(request):
    if request.method == 'POST':
        customer_id = Customer.objects.count() + 1
        customer_name = request.POST['name']
        customer_email = request.POST['email']
        if Customer.objects.filter(customer_email=customer_email).exists():
            return render(request, 'create_customer.html', {'message': 'Customer already exists!'})
        customer_phone = request.POST['phone']
        customer = Customer(customer_id=customer_id, customer_name=customer_name, customer_email=customer_email, customer_phone=customer_phone)
        customer.save()
        return render(request, 'create_customer.html', {'message': 'Customer added successfully!'})
    return render(request, 'create_customer.html')

def add_performers(request):
    if request.method == 'POST':
        performer_id = request.POST['performer_id']
        performer_name = request.POST['name']
        performer_genre = request.POST['genre']
        performer = Performer(performer_id=performer_id, performer_name=performer_name, performer_genre=performer_genre)
        performer.save()
        return render(request, 'add_performers.html', {'message': 'Performer added successfully!'})
    return render(request, 'add_performers.html')

def add_sponsors(request):
    if request.method == 'POST':
        sponsor_id = request.POST['sponsor_id']
        sponsor_name = request.POST['name']
        amount = request.POST['amount']
        sponsor = Sponsor(sponsor_id=sponsor_id, sponsor_name=sponsor_name, sponsor_amount=amount)
        sponsor.save()
        return render(request, 'add_sponsors.html', {'message': 'Sponsor added successfully!'})
    return render(request, 'add_sponsors.html')

def add_clubs(request):
    if request.method == 'POST':
        club_id = request.POST['club_id']
        club_name = request.POST['name']
        club = Club(club_id=club_id, club_name=club_name)
        club.save()
        return render(request, 'add_clubs.html', {'message': 'Club added successfully!'})
    return render(request, 'add_clubs.html')

def add_vendors(request):
    if request.method == 'POST':
        vendor_id = request.POST['vendor_id']
        vendor_name = request.POST['name']
        vendor_location = request.POST['location']
        vendor = Vendor(vendor_id=vendor_id, vendor_name=vendor_name, vendor_location=vendor_location)
        vendor.save()
        return render(request, 'add_vendor.html', {'message': 'Vendor added successfully!'})
    return render(request, 'add_vendor.html')

def event_sponsors(request):
    if request.method == 'POST':
        sponsor_name = request.POST['sponsor_name']
        sponsor = Sponsor.objects.get(sponsor_name=sponsor_name)
        event_name = request.POST['event_name']
        event = Event.objects.get(event_name=event_name)
        if EventSponsor.objects.filter(sponsor_id=sponsor, event_id=event).exists():
            return render(request, 'event_sponsors.html', {'message': 'Sponsor already exists!'})
        else:
            event_sponsor = EventSponsor(sponsor_id=sponsor, event_id=event)
            event_sponsor.save()
            return render(request, 'event_sponsors.html', {'message': 'Sponsor added successfully!', 'events': Event.objects.all(), 'sponsors': Sponsor.objects.all()})
    events = Event.objects.all()
    sponsors = Sponsor.objects.all()
    return render(request, 'event_sponsors.html', {'events': events, 'sponsors': sponsors})

def event_performers(request):
    if request.method == 'POST':
        performer_name = request.POST['performer_name']
        performer = Performer.objects.get(performer_name=performer_name)
        event_name = request.POST['event_name']
        event = Event.objects.get(event_name=event_name)
        if EventPerformer.objects.filter(performer_id=performer, event_id=event).exists():
            return render(request, 'event_performers.html', {'message': 'Performer already exists!'})
        else:
            event_performer = EventPerformer(performer_id=performer, event_id=event)
            event_performer.save()
            return render(request, 'event_performers.html', {'message': 'Performer added successfully!', 'events': Event.objects.all(), 'performers': Performer.objects.all()})
    events = Event.objects.all()
    performers = Performer.objects.all()
    return render(request, 'event_performers.html', {'events': events, 'performers': performers})

def event_clubs(request):
    if request.method == 'POST':
        club_name = request.POST['club_name']
        club = Club.objects.get(club_name=club_name)
        event_name = request.POST['event_name']
        event = Event.objects.get(event_name=event_name)
        if Organizes.objects.filter(club_id=club, event_id=event).exists():
            return render(request, 'event_clubs.html', {'message': 'Club already exists!'})
        else:
            event_club = Organizes(club_id=club, event_id=event)
            event_club.save()
            return render(request, 'event_clubs.html', {'message': 'Club added successfully!', 'events': Event.objects.all(), 'clubs': Club.objects.all()})
    events = Event.objects.all()
    clubs = Club.objects.all()
    return render(request, 'event_clubs.html', {'events': events, 'clubs': clubs})

def event_vendors(request):
    if request.method == 'POST':
        vendor_name = request.POST['vendor_name']
        vendor = Vendor.objects.get(vendor_name=vendor_name)
        event_name = request.POST['event_name']
        event = Event.objects.get(event_name=event_name)
        if EventVendor.objects.filter(vendor_id=vendor, event_id=event).exists():
            return render(request, 'event_vendors.html', {'message': 'Vendor already exists!'})
        else:
            event_vendor = EventVendor(vendor_id=vendor, event_id=event)
            event_vendor.save()
            return render(request, 'event_vendors.html', {'message': 'Vendor added successfully!', 'events': Event.objects.all(), 'vendors': Vendor.objects.all()})
    events = Event.objects.all()
    vendors = Vendor.objects.all()
    return render(request, 'event_vendors.html', {'events': events, 'vendors': vendors})
