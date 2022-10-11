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
            serial_number = form.cleaned_data['serial_number']
            item_number = form.cleaned_data['item_number']
            date = form.cleaned_data['date']
            commentary = form.cleaned_data['commentary']

            html = render_to_string('emails/email.html', {
                'type': type,
                'serial_number': serial_number,
                'item': item_number,
                'date': date,
                'commentary': commentary,
            }
            
            ) 
            send_mail('The contact form sub', 'Message', 'brunokoura@gmail.com', ['koura@weg.net'], html_message=html, fail_silently=False)
            
            return redirect('home')
    else:
        form = Form()
        
    return render(request, 'template.html', {
        'form': form 
    })
