from django import forms
from django.forms import ModelForm, Textarea
from events.models import Event, Publicevent


class GroupEventForm(forms.Form):
    CATEGORY = (
        ('pets', 'Pets'),
        ('kids', 'Kids'),)
    # user = forms.CharField(label='User Name', max_length=200)
    name = forms.CharField(label='Event Name', max_length=200)
    category = forms.ChoiceField(choices=CATEGORY)
    street = forms.CharField(label='Street', max_length=200)
    city = forms.CharField(label='City', max_length=200)
    state = forms.CharField(label='State', max_length=200)
    country = forms.CharField(label='Country', max_length=200)
    zipcode = forms.CharField(label='Zipcode', max_length=200)


class PublicEventForm(ModelForm):
    class Meta:
        model = Publicevent
        fields = ['address', 'name', 'banner', 'category']
        labels = {'address': ('Address'),
                  'name': ('Event Name'), 'banner': ('banner'), 'category': ('category')}
