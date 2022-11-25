from django import forms
from .component import component_type, material_type

class extraComponent(forms.Form):
    componentSelection= forms.ChoiceField(choices=component_type, label='Component Selection', required=True)
    componentQuantity = forms.IntegerField(label='Component Quantity', required=True)

class Form(forms.Form):
    branchName = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"size": 40, 'placeholder':'example@weg.net'}))
    name = forms.CharField(widget=forms.TextInput(attrs={"size": 50}))
    
    type = forms.ChoiceField(choices=material_type, initial="Select One Option")
    number = forms.CharField(label='Serial Number')

    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'dd/MM/YYYY'}), required=False)
    phase = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: SINGLE PHASE'}), required=False)
    capacity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: 15cv'}), required=False)
    centerQuantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ex: 2'}), required=False)

    # componentSelection= forms.ChoiceField(choices=component_type, label='Component Selection', required=True)
    # componentQuantity = forms.IntegerField(label='Component Quantity', required=True)

    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":200}))
    
class Extra:
    class Meta:
        model = extraComponent
        fields = (
            'componentSelection',
            'componentQuantity',
        )