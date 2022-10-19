from django import forms
import pandas as pd

material_type = (
    ('material', 'Search with material'),
    ('serial', 'Search with serial number'),
)

component_type = (
    ('A', 'TESTE1'),
    ('B', 'TESTE2'),
    ('C', 'TESTE3')
)


class Form(forms.Form):
    type = forms.ChoiceField(choices=material_type, initial="Select One Option")
    serialNumber = forms.CharField(label='Serial Number', required=False)
    itemNumber = forms.IntegerField(label='Item Number', required=False)
    date = forms.DateField(label='Manufactoring Date',widget=forms.DateInput(attrs={'placeholder':'Ex: 10/05/2022'}))
    phase = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Monophasic'}))
    capacity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: 15cv'}))
    centerQuantity = forms.IntegerField(label='Center Quantity')
    componentQuantity = forms.IntegerField(label='Component Quantity')
    componentSelection = forms.ChoiceField(choices=component_type, label='Component Selection')
    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}))
