from turtle import width
from django import forms
import pandas as pd

material_type = (
    ('material', 'Search with material'),
    ('serial', 'Search with serial number'),
)

component_type = (
    ('AIR FILTER', 'AIR FILTER'),
    ('ALUMINIUM FAN', 'ALUMINIUM FAN'),
    ('BEARING CAP DE', 'BEARING CAP DE')
)


class Form(forms.Form):
    type = forms.ChoiceField(choices=material_type, initial="Select One Option")
    serialNumber = forms.CharField(label='Serial Number', required=False)
    itemNumber = forms.IntegerField(label='Item Number', required=False)
    date = forms.DateField(label='Manufactoring Date',widget=forms.DateInput(attrs={'placeholder':'Ex: 10/05/2022'}))
    phase = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Monophasic'}))
    capacity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: 15cv'}))
    centerQuantity = forms.IntegerField(label='Center Quantity')
    componentSelection = forms.ChoiceField(choices=component_type, label='Component Selection')
    componentQuantity = forms.IntegerField(label='Component Quantity')
    componentSelection1 = forms.ChoiceField(choices=component_type, label='Component Selection', required=False)
    componentQuantity1 = forms.IntegerField(label='Component Quantity', required=False)
    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}))
    
