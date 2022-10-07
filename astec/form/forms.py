from xmlrpc.client import boolean
from django import forms


material_type = (
    ('S', 'Select one option'),
    ('M', 'Search with material'),
    ('SN', 'Search with serial number'),
)

class Form(forms.Form):
    code = forms.CharField(max_length=50)
    email = forms.EmailField()
    name = forms.CharField(max_length=50)
    type = forms.ChoiceField(choices=material_type)
    serial_number = forms.CharField()
    item_number = forms.IntegerField()
    date = forms.DateField()
    commentary = forms.CharField(widget=forms.Textarea())

