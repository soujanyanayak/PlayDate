from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def groups(request):
    return render(request, "groups/groups.html")


def createGroup(request):
    return render(request, "groups/createGroup.html")
