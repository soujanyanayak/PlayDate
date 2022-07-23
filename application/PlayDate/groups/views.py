#••••••••••••••••••••••••••••••••••••••••••#
# ░█▀▀░█▀▄░█▀█░█░█░█▀█░░░█░█░▀█▀░█▀▀░█░█░█▀▀
# ░█░█░█▀▄░█░█░█░█░█▀▀░░░▀▄▀░░█░░█▀▀░█▄█░▀▀█
# ░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░░░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀
# Contributor(s): AndrewC,
# Version: 1.5.1
# Homepage: http://bedev.playdate.surge.sh/docs/groups/views
# Description: A core functionality of playdate; the views in this file dictate how groups
# are handled by our application including joining/leaving, posting events/comments,
# CRUD operations on group entities, and groupAdmin functionalities.
#•••••••••••••••••••••••••••••••••••••••••••#

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from . import forms


def Search(request):
    if 'search' in request.GET:
        query = request.GET['search'].split()
        print("\nQuery:", query)
        groups = models.Group.objects.filter(tags__name__in=query).distinct()
        print(groups)
        return render(request, "groups/groupSearch.html", {'groups': groups})
    return render(request, "groups/groupSearch.html")

# This view is the main driver for groups; it is by far the biggest view
# It has three parts: 1 for a group member, 1 for an non-member, and 1 for the non-user


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

    # This represents the part of the page for a member of the group.
    # Contains functionality for view/crud posts
    # if isMember == True:
    # The following 2 if-statements correspond to joining a group and leaving a group
    if isMember == False:
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
    if isMember == True:
        if 'leaveGroup' in request.POST:
            removeMember = models.Member.objects.filter(
                group_id=group_id, member_id=request.user).delete()
            isMember = False
            print(request.user, 'has left group:', group.group_name)
            return render(request, "groups/groups.html", {'group': group, 'member_list': member_list, 'isMember': isMember, })
            # return redirect('joinSuccess') //This does not work but should be reimplemented because its better practice

    return render(request, "groups/groups.html", {'group': group, 'member_list': member_list, 'isMember': isMember})


def createGroup(request):
    createGroupForm = forms.createGroupForm()
    memberListForm = forms.memberListForm()
    if request.method == 'POST':
        createGroupForm = forms.createGroupForm(request.POST, request.FILES)
        print("FILES", request.FILES)
        memberListForm = forms.memberListForm(request.POST)
        if createGroupForm.is_valid() and memberListForm.is_valid():
            instanceGroup = createGroupForm.save(commit=False)
            instanceGroup.group_admin = request.user
            instanceGroup.banner = None
            # the if-stmt below is for when the groupCreator doesn't upload a group banner
            if request.FILES == '':
                instanceGroup.banner = request.FILES['']
            # otherwise they did upload a banner
            else:
                instanceGroup.banner = request.FILES['banner']
            instanceGroup.save()
            # put the title in the tags

            groupName = str(instanceGroup.group_name).split()
            print(groupName)

            createGroupForm.save_m2m()

            instanceMember = memberListForm.save(commit=False)
            instanceMember.group_id = instanceGroup
            instanceMember.member_id = request.user
            instanceMember.save()

            group = models.Group.objects.get(
                group_id=instanceGroup.group_id)
            member_list = models.Member.objects.filter(
                group_id=instanceGroup.group_id)
            # print(member_list.member_id)
            isMember = True
            for titleWord in groupName:
                group.tags.add(titleWord)

            return render(request, 'groups/groups.html', {'group': group, 'member_list': member_list, 'isMember': isMember})

    return render(request, 'groups/createGroup.html', {'createGroupForm': createGroupForm, 'memberListForm': memberListForm})

# •NOTE•
# Remove the following 4 methods once main functionalities are implemented
# and then reroute the URLs to the correct paths

# DEV USE ONLY


def testGroup(request):
    return render(request, "groups/testGroup.html")

# STATIC: PROTOTYPE USE ONLY


def searchResults(request):
    return render(request, "groups/searchResults.html")

# STATIC: PROTOTYPE USE ONLY


def individualGroup(request):
    return render(request, "groups/individualGroup.html")

# STATIC: PROTOTYPE USE ONLY


def myGroup(request):
    return render(request, "groups/myGroup.html")

# STATIC: PROTOTYPE USE ONLY


def groups(request):
    # The code in this function is the startercode for the group search
    # groupList = models.Group.objects.order_by('-group_id')[:]

    # return render(request, "groups/viewAllGroups.html", {'groupList': groupList})
    return render(request, "groups/viewAllGroups.html")
# ••••••


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
