from django.shortcuts import render, redirect
from django.http import HttpResponse
from ipware import get_client_ip
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models
from . import forms
# Create your views here.

# This is used to manage and track sessions.
# Session information is serialized via JSON_Serializer and stored in django_session
# needs fine-tuning in order to better track sessions for unlogged and logged users.


def sessionCreation(request):
    if not request.session.session_key:
        request.session.create()
        # session time is set to 6minutes, needs to be updated
        request.session.set_expiry(360)
        request.session['visitorIP'] = get_client_ip(request)[0]
        print("session created for IP: ",
              request.session['visitorIP'], " with tracking_key:", request.session.session_key)


def home(request):
    sessionCreation(request)
    print(request.session.session_key)
    # userData = request.user
    # if userData.is_authenticated:
    #     userInfo = User.objects.get(username=userData)

    #     accountInfo = models.Account.objects.get(accountID=userInfo.id)

    #     print(userData)
    #     userID = userInfo.id
    #     lastLogin = userInfo.last_login
    #     is_superuser = userInfo.is_superuser
    #     fname = userInfo.first_name
    #     lname = userInfo.last_name
    #     email = userInfo.email

    #     gender = accountInfo.gender
    #     dob = accountInfo.dob
    #     print(is_superuser)
    #     print(lastLogin)
    #     print(userID)
    #     print(gender)
    #     return render(request, 'home/home.html', {'userID': userID, 'fname': fname, 'lname': lname, 'email': email, 'gender': gender, 'dob': dob})
    #     if(request.get('logoutBTN')):
    #         logout(request.user)
    #     return render(request, 'home/logout.html')
    # else:
    #     return render(request, 'home/home.html')

    return render(request, 'home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
            # return render(request, 'login.html')

    context = {}
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return render(request, 'home.html')


def registrationPage(request):
    sessionCreation(request)
    # print(request.session.session_key)
    # print(request.session['visitorIP'])
    user_form = forms.userRegistrationForm()
    accountForm = forms.accountForm()

    if request.method == 'POST':
        sessionCreation(request)
        user_form = forms.userRegistrationForm(request.POST)
        accountForm = forms.accountForm(request.POST)

        if user_form.is_valid() and accountForm.is_valid():
            user = user_form.save()
            account = accountForm.save(commit=False)
            account.accountID = user.id
            account.save()
            account.trackingID = request.session.session_key
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            account.save()
            if user is not None:
                login(request, user)
                userData = request.user
                userInfo = User.objects.get(username=username)
                accountInfo = models.Account.objects.get(accountID=userInfo.id)
                login(request, user)
                userID = userInfo.id
                lastLogin = userInfo.last_login
                is_superuser = userInfo.is_superuser
                fname = userInfo.first_name
                lname = userInfo.last_name
                email = userInfo.email
                gender = accountInfo.gender
                dob = accountInfo.dob

                return render(request, "home.html", {'userID': userID, 'fname': fname, 'lname': lname, 'email': email, 'gender': gender, 'dob': dob})
            else:
                return render(request, "invalidLogin.html")

    return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm})


def publicPage(request):
    return render(request, 'public.html')

def helpPage(request):
    return render(request, 'helpPage.html')

def termsofuse(request):
        return render(request, 'termsofuse.html')

def privacy(request):
        return render(request, 'privacy.html')