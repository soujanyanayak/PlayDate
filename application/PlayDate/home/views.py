from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models
from . import forms
# Create your views here.


def home(request):
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

    return render(request, 'home/home.html')


def loginPage(request):
    return render(request, 'home/login.html')


def logoutPage(request):
    return render(request, 'home/logout.html')


def registrationPage(request):
    user_form = forms.userRegistrationForm()
    accountForm = forms.accountForm()

    if request.method == 'POST':
        user_form = forms.userRegistrationForm(request.POST)
        accountForm = forms.accountForm(request.POST)

        if user_form.is_valid() and accountForm.is_valid():
            user = user_form.save()
            account = accountForm.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            account.save()

            if user is not None:
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

                return render(request, "home/home.html", {'userID': userID, 'fname': fname, 'lname': lname, 'email': email, 'gender': gender, 'dob': dob})
            else:
                return render(request, "home/invalidLogin.html")

    return render(request, 'home/register.html', {'user_form': user_form, 'accountForm': accountForm})
