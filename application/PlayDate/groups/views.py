from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def groups(request):
    return HttpResponse("groups")


def createGroup(request):
    return HttpResponse("group create")
