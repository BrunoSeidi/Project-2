from django import forms

material = 1
serial = 2

material_type = (
    (material, 'Search with material'),
    (serial, 'Search with serial number'),
)

component_type = (
    ('A', 'TESTE1'),
    ('B', 'TESTE2'),
    ('C', 'TESTE3')
)


class Form(forms.Form):
    type = forms.ChoiceField(choices=material_type)
    serialNumber = forms.CharField(label='Serial Number')
    itemNumber = forms.IntegerField(label='Item Number')
    date = forms.DateField(label='Manufactoring Date',widget=forms.DateInput(attrs={'placeholder':'Ex: 10/05/2022'}))
    phase = forms.CharField()
    capacity = forms.CharField()
    centerQuantity = forms.IntegerField(label='Center Quantity')
    componentQuantity = forms.IntegerField(label='Component Quantity')
    componentSelection = forms.ChoiceField(choices=component_type, label='Component Selection')
    commentary = forms.CharField(widget=forms.Textarea(attrs={"rows":8, "cols":80}))
