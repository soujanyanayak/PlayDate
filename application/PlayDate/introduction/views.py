from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    #return HttpResponse("Hello, world. You're at the introduction index.")
    template = loader.get_template('list_view.html')
    return HttpResponse(template.render())

def soujanya(request):
    #return HttpResponse("Hello, world. You're at the introduction index.")
    template = loader.get_template('soujanya_view.html')
    return HttpResponse(template.render())
    
def qing(request):
    #return HttpResponse("Hello, world. You're at the introduction index.")
    template = loader.get_template('qing_view.html')
    return HttpResponse(template.render())

def about(request):
    #return HttpResponse("Hello, world. You're at the introduction index.")
    template = loader.get_template('about_view.html')
    return HttpResponse(template.render())