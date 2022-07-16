# from cgitb import lookup
from multiprocessing import Event
from unicodedata import category
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from events.forms import GroupEventForm
from events.models import  Publicevent, Address, Event
from django.views.decorators.csrf import csrf_exempt

import requests
from bs4 import BeautifulSoup

# Create your views here.

def publicevents(request):
    publicevent = Publicevent.objects.all()
    return render(request,"publicevents.html",{'publicevent':publicevent})

def myevents(request):
    # publicevent = Publicevent.objects.all()
    return render(request,"myevents.html")

@csrf_exempt
def createUserEvent(request):
    # publicevent = Publicevent.objects.all()
    return render(request,"createuserevent.html")

@csrf_exempt
def createGroupEvent(request):
    if request.method == 'POST':
        form = GroupEventForm(request.POST)
        if form.is_valid():
            a=Address.objects.create(street=request.POST.get('street'),
            city=request.POST.get('city'), 
            state=request.POST.get('state'), 
            country=request.POST.get('country'),
            zipcode=request.POST.get('zipcode') )
            ge=Event.objects.create(name=request.POST.get('name'),event_url=request.POST.get('event_url'), category=request.POST.get('category'),address= a)

            return HttpResponseRedirect('/thanks/')
    else:
        form = GroupEventForm()

    return render(request, "createEvent.html", {'form':form})


def filter(request):
    if request.method == 'POST':
        select= request.GET.get('select')
        


# Returns Search result for events
def events(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        filter= request.GET.get('category')
        
        submitbutton= request.GET.get('submit')
        print(query)
        
        if query is not None:
            if filter=='All': 
           #query databse to check if matching city, zipcode, or street
           
                lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

                results= Publicevent.objects.filter(lookups)
            
            elif filter=='Kids': 
            #query databse to check if matching city, zipcode, or street
            
                lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

                results= Publicevent.objects.filter(lookups).filter(Q(category__icontains = 'kids'))
                print(filter)
            else:
                lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

                results= Publicevent.objects.filter(lookups).filter(Q(category__icontains = 'pets'))
                
            
            context={'results': results,
                     'submitbutton': submitbutton}
           
            return render(request, 'events/events.html', context)
        
        
        
    else:
        return render(request, 'events/events.html')
    return render(request, 'events/events.html')
    





