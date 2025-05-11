from django.shortcuts import redirect, render
from django.http import HttpResponse
import random

from .models import *

# Create your views here.
# def index(request):
    # return HttpResponse("Hello World")

def index(request):    
    return render(request, 'home.html')

def submitTickets(request): 
    tasks = Tickets.objects.all()
    ticketNumber = random.getrandbits(28)
    context = {'tasks':tasks, 'ticketNumber':ticketNumber}

    if request.method == 'POST':
        number = request.POST.get('number')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        description = request.POST.get('description')

        # ✅ Basic Validation
        if not number or not status or not priority or not description:
            return HttpResponse("All fields are required.", status=400)

        # 💾 Optional: Save to database
        Tickets.objects.create(number=number, status=status, priority=priority,description=description)

        return HttpResponse("Form submitted successfully!") 
    return render(request, 'submitTickets.html', context)

def checkTicketsStatus(request):  
    if request.method == 'POST':
        ticketNumber = request.POST.get('ticketNumber')
        listOfTickets = Tickets.objects.filter(number=ticketNumber)
        # ✅ Basic Validation
        if not ticketNumber :
            return HttpResponse("All fields are required.", status=400)
        context = {'listOfTickets':listOfTickets}
        return render(request, 'checkTicketStatus.html',context)  
    return render(request, 'checkTicketStatus.html')

def listOfTickets(request):  
    tickets = Tickets.objects.all()
    context = {'tickets':tickets}  
    return render(request, 'listOfTickets.html', context)