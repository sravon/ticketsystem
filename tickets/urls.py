from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import path

from tickets import views

from .models import *

# Create your views here.
# def index(request):
    # return HttpResponse("Hello World")

urlpatterns = [
    path('', views.index),
    path('submit-ticket', views.submitTickets),
    path('check-ticket-status', views.checkTicketsStatus),
    path('list-of-tickets', views.listOfTickets),
    path('delete/<int:ticket_id>/', views.deleteTicket, name='delete_task'),
]