from django import forms
from django.db import models

from .component import component_type, material_type



class Extra(models.Model):
    choices = models.CharField(choices=component_type, max_length=50)
    quantity = models.IntegerField()

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

    componentSelection= forms.ChoiceField(choices=component_type, label='Component Selection', required=True)
    componentQuantity = forms.IntegerField(label='Component Quantity', required=True)
    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":200}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        extrafield = Extra.objects.filter(
    )
        for i in range(len(extrafield) + 1):
            choices_field = 'choices_%s' % (i,)
            self.fields[choices_field] = forms.ChoiceField(required=False)
            try:
                self.initial[choices_field] = extrafield[i].choices
            except IndexError:
                self.initial[choices_field] = ""
        # create an extra blank field
        choices_field = 'choices_%s' % (i + 1,)
        self.fields[choices_field] = forms.CharField()

class Form2(forms.Form):
    age = forms.IntegerField()