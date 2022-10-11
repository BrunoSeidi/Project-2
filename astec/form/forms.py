from random import choices
from xmlrpc.client import boolean
from django import forms


material_type = (
    ('S', 'Select one option'),
    ('M', 'Search with material'),
    ('SN', 'Search with serial number'),
)

component_type = (
    ('A', 'TESTE1'),
    ('B', 'TESTE2'),
)


class Form(forms.Form):
    type = forms.ChoiceField(choices=material_type)
    serialNumber = forms.CharField(label='Serial Number')
    itemNumber = forms.IntegerField(label='Item Number')
    date = forms.DateField()
    phase = forms.CharField()
    capacity = forms.CharField()
    centerQuantity = forms.IntegerField(label='Center Quantity')
    componentQuantity = forms.IntegerField(label='Component Quantity')
    componentSelection = forms.ChoiceField(choices=component_type, label='Component Selection')
    commentary = forms.CharField(widget=forms.Textarea())
