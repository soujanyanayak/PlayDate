from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
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
        profileForm = forms.profileForm(request.POST)
        if user_form.is_valid() and accountForm.is_valid() and profileForm.is_valid():
            user = user_form.save()
            account = accountForm.save(commit=False)
            account.accountID = user
            account.save()
            account.trackingID = request.session.session_key
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            account.save()
            if user is not None:
                login(request, user)
                # trying to figure out how to put the next 3 lines above 'if user is not None'
                profile = profileForm.save(commit=False)
                profile.profileID = request.user
                profile.save()

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
        else:
            print (user_form.errors)
            return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm, 'error': user_form.errors})

    return render(request, 'register.html', {'user_form': user_form, 'accountForm': accountForm})


def profileEditPage(request):
    profile = models.Profile.objects.get(profileID=request.user)
    print(profile.avatar)
    profileForm = forms.profileForm()
    if request.method == 'POST':
        profileForm = forms.profileForm(request.POST, request.FILES)
        if profileForm.is_valid():
            instance = profileForm.save(commit=False)
            instance.profileID = request.user
            # Delete current avatar and replace it with request.FILES['avatar']
            instance.avatar = None
            instance.avatar = request.FILES['avatar']
            print(instance.avatar)
            # Update profile in database
            instance.save()

            profile = models.Profile.objects.get(profileID=request.user)
            return render(request, 'profilePage.html', {'profileForm': profileForm, 'profile': profile})
    else:
        profileForm = forms.profileForm()
    return render(request, 'profileEdit.html', {'profileForm': profileForm, 'profile': profile})


def profilePage(request):
    profile = models.Profile.objects.get(profileID=request.user)
    # print(profile)
    return render(request, 'profilePage.html', {'profile': profile})


def profileView(request, profile_id):
    profile = models.Profile.objects.get(profileID=profile_id)
    account = models.Account.objects.get(accountID=profile_id)
    return render(request, 'profileView.html', {'profile': profile, 'account': account})


def individuleInfoPage(request):
    return render(request, 'individuleInfo.html')


def helpPage(request):
    return render(request, 'helpPage.html')


def termsofuse(request):
    return render(request, 'termsofuse.html')


def privacy(request):
    return render(request, 'privacy.html')


def comesoonPage(request):
    return render(request, 'comeSoon.html')

def myGroupsPage(request):
    return render(request, 'myGroupsPage.html')

def contactSupport(request):
    csForm = forms.supportForm()
    print ('*******************************')
    print ('Support Contact form Submitted by ' + request.user.get_username())
    if request.method == 'POST':
        print (request.POST)
        csForm = forms.supportForm(request.POST)
        if csForm.is_valid():
            print('Form is valid.')
            ticket = csForm.save(commit=False)

            # Grab Registered user data
            if request.user.is_authenticated:
                ticket.accountID = request.user
                print ('User is authenticated: ' + request.user.username)

            # Grab General User Data
            ipAddr = request.META['REMOTE_ADDR']
            print ('IP Address: ' + str(ipAddr))
            try:
                print('Trying to fill General User...')
                userQuery = models.generalUser.objects.get(ip=ipAddr)
                print ('Query Success...')
                userInfo = userQuery.first()
                print ('Using general user: ' + userInfo)
            except:
                print ('Exception Caught - Query Error')
                userInfo = models.generalUser(ip=ipAddr)
                userInfo.save()
                print ('Using new General User: ' + userInfo.ip)
            else:
                print ("General User found")
            finally:
                ticket.general = userInfo
                # Grab Support Staff Data
                try: 
                    print('Trying to fill support staff...')
                    staffQuery = models.Supportstaff.objects.all()
                    print('Query Success...')
                    staffInfo = staffQuery.first()
                    print ('Using Staff: ' + staffInfo.staff_email +'\n')
                    status = 'Success'
                    ticket.staff = staffInfo
                except:
                    print ("No staff to send support request to")
                    status = 'No Staff'
                finally:
                    ticket.save()
                    print(ticket)
                    if status == 'Success':
                        email_subject = 'PlayDate Support #' + str(ticket.request_id) + ': ' + ticket.name
                        email_content = email_subject + '\n';
                        email_content += 'User: '
                        if request.user.is_authenticated:
                            email_content += request.user.get_username()
                        else:
                            email_content += ipAddr
                        email_content += '\nEmail: ' + ticket.accountID.email + '\n'
                        email_content += 'Category: ' + ticket.get_type_display() + '\n'
                        email_content += 'Details: \n\t' + ticket.details + '\n\n'
                        email_from = 'support@playdate.com'
                        email_to = staffInfo.staff_email
                        print('Email Description: ')
                        print("Subject: " + email_subject)
                        print("Content: " + email_content)
                        print("From: " + email_from)
                        print("To: " + email_to)
                        send_mail(
                            email_subject,
                            email_content, 
                            email_from,
                            [email_to],
                            fail_silently=True
                        )
                    return render(request, 'contactSupport.html', { 'csForm': csForm, 'status': status})
    return render(request, 'contactSupport.html', {'csForm': csForm})