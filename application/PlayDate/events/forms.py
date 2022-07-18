from django import forms



class GroupEventForm(forms.Form):
    CATEGORY=(
    ('pets','Pets'),
    ('kids','Kids'),)
    name = forms.CharField(label='Event Name', max_length=200)
    category = forms.ChoiceField(choices=CATEGORY)
    street = forms.CharField(label='Street', max_length=200)
    city = forms.CharField(label='City', max_length=200)
    state = forms.CharField(label='State', max_length=200)
    country = forms.CharField(label='Country', max_length=200)
    zipcode = forms.CharField(label='Zipcode', max_length=200)

