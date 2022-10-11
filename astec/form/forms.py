from random import choices
from xmlrpc.client import boolean
from django import forms


material_type = (
    ('S', 'Select one option'),
    ('M', 'Search with material'),
    ('SN', 'Search with serial number'),
)

component_type = (
    ('A', 'TESTE1')
    ('B', 'TESTE2')
)


class Form(forms.Form):
    type = forms.ChoiceField(choices=material_type)
    serial_number = forms.CharField()
    item_number = forms.IntegerField()
    date = forms.DateField()
    fase = forms.CharField()
    capacity = forms.IntegerField()
    center_quantity = forms.IntegerField(label='Center Quantity')
    component_quantity = forms.IntegerField(label='Quantity')
    component_selection = forms.ChoiceField(choices=component_type, label='Component Selection')
    commentary = forms.CharField(widget=forms.Textarea())
