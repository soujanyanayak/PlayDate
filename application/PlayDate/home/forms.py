from django import forms
from django.forms import ModelForm, Textarea, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class profileForm(ModelForm):
    class Meta:
        model = models.Profile
        #exclude = ('profileDesc', 'avatar',)
        fields = ['profileDesc', 'avatar']
        labels = {
            'profileDesc': ('Profile Description'), 'avatar': ('Avatar'),
        }

class profileVerificationForm(ModelForm):
    # clean_image is a workaround to server-side
    # validate the verification image.
    def clean_image(self):
        verImg = self.cleaned_data['verification']
        if verImg:
            # size measured in bytes
            if verImg.size > 6.5 * 1048578:
                raise ValidationError("Verification image must be under 6.5 MB")
            verImgExt = verImg.name.split('.')[-1]
            allowedTypes = "apng, avif, gif jpeg, jpg, png, webp"
            if verImgExt in allowedTypes:
                return verImg
            raise ValidationError("Verification image in the wrong format.")
        raise ValidationError("No verification image uploaded.")

    class Meta:
        model = models.Profile
        fields = ['verification']
        labels = {'verification': ('Verification Document')}

class userRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        model.is_staff = False
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class accountForm(ModelForm):
    class Meta:
        model = models.Account
        fields = ['gender', 'dob']
        labels = {
            'dob': ('D. O. B.'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class supportForm(ModelForm):
    class Meta:
        model = models.Requestsupport
        fields = ['contact', 'name', 'type', 'details']
        labels = {
            'contact': ('Your Email or Phone'),
            'name': ('Name of the Issue'),
            'type': ('Support Category'),
            'details':  ('Please provide detail of the issue')
        }

class addressForm(ModelForm):
    class Meta:
        model = models.Address
        fields = ['street', 'state', 'country','zipcode','city']
        labels={
            'street':('Street/Building'),
            'state':('State'),
            'country':('Country'),
            'zipcode':('Zipcode'),
            'city':('City')
        }
