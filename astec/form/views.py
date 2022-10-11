import email
from django.shortcuts import render, redirect
from .forms import Form
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
    # code = forms.CharField(max_length=50)
    # email = forms.EmailField()
    # name = forms.CharField(max_length=50)
    # type = forms.ChoiceField(choices=material_type)
    # serial_number = forms.CharField()
    # item_number = forms.IntegerField()
    # date = forms.DateField()
    # commentary = forms.CharField(widget=forms.Textarea())
def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        
        if form.is_valid():
            type = form.cleaned_data['type']
            serialNumber = form.cleaned_data['serialNumber']
            itemNumber = form.cleaned_data['itemNumber']
            date = form.cleaned_data['date']
            phase = form.cleaned_data['phase']
            capacity = form.cleaned_data['capacity']
            centerQuantity = form.cleaned_data['centerQuantity']
            componentQuantity = form.cleaned_data['componentQuantity']
            componentSelection = form.cleaned_data['componentSelection']
            commentary = form.cleaned_data['commentary']


            html = render_to_string('emails/email.html', {
                'type': type,
                'serialNumber': serialNumber,
                'item': itemNumber,
                'date': date,
                'phase':phase,
                'capacity':capacity,
                'centerQuantity':centerQuantity,
                'componentQuantity':componentQuantity,
                'componentSelection': componentSelection,
                'commentary': commentary,
            }
            
            ) 
            send_mail('The contact form sub', 'Message', 'noreply@weg.net', ['koura@weg.net'], html_message=html, fail_silently=False)
            
            return redirect('home')
    else:
        form = Form()
        
    return render(request, 'template.html', {
        'form': form 
    })
