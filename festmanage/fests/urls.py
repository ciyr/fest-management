from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('addEvents/', views.addEvents, name='addEvents'),
    path('buy_tickets/', views.buy_tickets, name='buy_tickets'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('add_performers/', views.add_performers, name='add_performers'),
    path('add_sponsors/', views.add_sponsors, name='add_sponsors'),
    path('add_clubs/', views.add_clubs, name='add_clubs'),
    path('add_vendors/', views.add_vendors, name='add_vendors'),
    path('event_sponsors/', views.event_sponsors, name='event_sponsors'),
    path('event_performers/', views.event_performers, name='event_performers'),
    path('event_clubs/', views.event_clubs, name='event_clubs'),
    path('event_vendors/', views.event_vendors, name='event_vendors'),
]

