# from cgitb import lookup
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from events.models import  Publicevent, Address

import requests
from bs4 import BeautifulSoup

# Create your views here.


# def searchevents(city):
#     state=''

#     URL = "https://www.eventbrite.com/d/"+state+"--"+city+"/dog-events/"
    
#     page = requests.get(URL)

#     soup = BeautifulSoup(page.content, "html.parser")

#     results=soup.find_all("div", {"class": "eds-event-card-content__content"})
#     events=[]
#     #print(page.text)
#     #print("\n\n\n\n\n")
#     for item in results:
#         #print(item.prettify())
#         links = item.find_all('a')
#         blog_titles = item.findAll('h3', attrs={"class":"eds-event-card-content__title eds-text-color--ui-800 eds-text-bl eds-text-weight--heavy"})
#         venue = item.findAll("div", {"data-subcontent-key":"location"})
#         #print(links)
#         url=''
#         location=''
#         for link in links:
#             if "href" in link.attrs:
#                 url=link.attrs['href']
#         for loc in venue:
#             location=loc.text
#         for title in blog_titles:
#             if str(title.text).find('Dog') != -1:
#                 event={}
#                 event['title']= str(title.text)
#                 event['url']=str(url)
#                 event['location']=str(location)
#                 event['source']="Eventbrite"
#                 events.append(event)
#     return events


def createEvent(request):
    return render(request, "events/createEvent.html")


def events(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        print(query)
        submitbutton= request.GET.get('submit')

        if query is not None: 
            # context={'results': searchevents(query),'submitbutton': submitbutton}
            #result=Event.objects.select_related('location')

            #print(query)
           
            lookups= Q(address__city__icontains=query) | Q(address__zipcode__icontains=query) | Q(address__country__icontains=query) | Q(address__street__icontains=query)

            results= Publicevent.objects.filter(lookups)
            results = Publicevent.objects.filter(lookups).select_related('address')

            context={'results': results,
                     'submitbutton': submitbutton}
            

            return render(request, 'events/events.html', context)

        else:
            return render(request, 'events/events.html')

    else:
        return render(request, 'events/events.html')





