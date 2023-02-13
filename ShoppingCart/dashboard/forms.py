from django import forms 

class ShippingDetailsForm(forms.Form):
    address = forms.Textarea()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.CharField()