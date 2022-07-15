#  _______ .______        ______    __    __  .______     _______.
# /  _____||   _  \      /  __  \  |  |  |  | |   _  \   /       |
# |  |  __  |  |_)  |    |  |  |  | |  |  |  | |  |_)  | |   (----`
# |  | |_ | |      /     |  |  |  | |  |  |  | |   ___/   \   \
# |  |__| | |  |\  \----.|  `--'  | |  `--'  | |  |   .----)   |
# \______| | _| `._____| \______/   \______/  | _|   |_______/
#
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from . import forms


def groups(request):
    # The code in this function is the startercode for the group search
    groupList = models.Group.objects.order_by('-group_id')[:]

    return render(request, "groups/viewAllGroups.html", {'groupList': groupList})


def groupView(request, group_id):
    joinGroupForm = forms.joinGroupForm()
    group = models.Group.objects.get(
        group_id=group_id)
    member_list = models.Member.objects.filter(group_id=group_id)

    # isMember first checks if the user is logged in, then checks the Member table for the (group_id, user_id), returns True is they are a member
    isMember = False
    if request.user.is_authenticated:
        if len(models.Member.objects.filter(group_id=group_id, member_id=request.user)) == 1:
            isMember = True
            # print(isMember)
    if not request.user.is_authenticated:
        print("user is not authenticated")

    # The following 2 if-statements correspond to joining a group and leaving a group
    if 'joinGroup' in request.POST:
        print(request.method)
        joinGroupForm = forms.joinGroupForm(request.POST)
        instanceMember = joinGroupForm.save(commit=False)
        instanceMember.group_id = models.Group.objects.get(
            group_id=group_id)
        instanceMember.member_id = request.user
        instanceMember.save()
        isMember = True
        print(request.user, 'has joined group:', group.group_name)
        return render(request, "groups/groups.html", {'group': group, 'member_list': member_list, 'isMember': isMember, })
    if 'leaveGroup' in request.POST:
        removeMember = models.Member.objects.filter(
            group_id=group_id, member_id=request.user).delete()
        isMember = False
        print(request.user, 'has left group:', group.group_name)
        return render(request, "groups/groups.html", {'group': group, 'member_list': member_list, 'isMember': isMember, })
        # return redirect('joinSuccess') //This does not work but should be reimplemented because its better practice

    return render(request, "groups/groups.html", {'group': group, 'member_list': member_list, 'isMember': isMember})


def joinSuccess(request, group_id):
    # ░█▀▄░█▀▀░█▀█░█▀█░▀█▀░█▀▄░░░█▀█░█▀▀░█▀▀░█▀▄░█▀▀░█▀▄
    # ░█▀▄░█▀▀░█▀▀░█▀█░░█░░█▀▄░░░█░█░█▀▀░█▀▀░█░█░█▀▀░█░█
    # ░▀░▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░
    # MAINTENENCE - instead for now just redirect user to the updated group page being joining group
    # group = models.Group.objects.get(group_id=group_id)
    # print("hello", group)
    # return render(request, "groups/joinSuccess.html", {'group': group})
    print("Maintenence")
    return HttpResponse("404 Maintenence")


def createGroup(request):
    createGroupForm = forms.createGroupForm()
    memberListForm = forms.memberListForm()
    if request.method == 'POST':
        createGroupForm = forms.createGroupForm(request.POST)
        memberListForm = forms.memberListForm(request.POST)
        if createGroupForm.is_valid() and memberListForm.is_valid():
            instanceGroup = createGroupForm.save(commit=False)
            instanceGroup.group_admin = request.user
            instanceGroup.save()

            instanceMember = memberListForm.save(commit=False)
            instanceMember.group_id = instanceGroup
            instanceMember.member_id = request.user
            instanceMember.save()

            group = models.Group.objects.get(
                group_id=instanceGroup.group_id)
            return render(request, 'groups/groups.html', {'group': group})

    return render(request, 'groups/createGroup.html', {'createGroupForm': createGroupForm, 'memberListForm': memberListForm})
