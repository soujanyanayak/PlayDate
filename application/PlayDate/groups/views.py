from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from . import forms
# Create your views here.


def groups(request):

    return render(request, "groups/groups.html")


def createGroup(request):
    # print(request.user)
    createGroupForm = forms.createGroupForm()
    memberListForm = forms.memberListForm()
    if request.method == 'POST':
        createGroupForm = forms.createGroupForm(request.POST)
        memberListForm = forms.memberListForm(request.POST)
        if createGroupForm.is_valid() and memberListForm.is_valid():
            instanceGroup = createGroupForm.save(commit=False)
            instanceGroup.groupAdminID = request.user
            instanceGroup.save()

            instanceMember = memberListForm.save(commit=False)
            instanceMember.groupID = instanceGroup
            instanceMember.memberID = request.user
            instanceMember.save()

            group = models.Group.objects.get(
                groupID=instanceGroup.groupID)
            return render(request, 'groups/groups.html', {'group': group})

    return render(request, 'groups/createGroup.html', {'createGroupForm': createGroupForm, 'memberListForm': memberListForm})
