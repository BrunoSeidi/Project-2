from logging import PlaceHolder
from django import forms
from .component import component_type, material_type


class Form(forms.Form):
    branchName = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"size": 40}))
    name = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))
    
    type = forms.ChoiceField(choices=material_type, initial="Select One Option")
    serialNumber = forms.CharField(label='Serial Number', required=False)
    itemNumber = forms.IntegerField(label='Item Number', required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Ex: 10/05/2022'}), required=False)
    phase = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: SINGLE PHASE'}))
    capacity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: 15cv'}))
    centerQuantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '2'}))

    componentSelection = forms.ChoiceField(choices=component_type, label='Component Selection', required=True)
    componentQuantity = forms.IntegerField(label='Component Quantity', required=True)
    componentSelection1 = forms.ChoiceField(choices=component_type, label='Component Selection', required=False)
    componentQuantity1 = forms.IntegerField(label='Component Quantity,', required=False)
    componentSelection2 = forms.ChoiceField(choices=component_type, label='Component Selection', required=False)
    componentQuantity2 = forms.IntegerField(label='Component Quantity', required=False)
    componentSelection3 = forms.ChoiceField(choices=component_type, label='Component Selection', required=False)
    componentQuantity3 = forms.IntegerField(label='Component Quantity', required=False)
    componentSelection4 = forms.ChoiceField(choices=component_type, label='Component Selection', required=False)
    componentQuantity4 = forms.IntegerField(label='Component Quantity', required=False)
    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":200}))




