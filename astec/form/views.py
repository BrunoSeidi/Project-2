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
            code = form.cleaned_data['code']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            serial_number = form.cleaned_data['serial_number']
            item_number = form.cleaned_data['item_number']
            date = form.cleaned_data['date']
            commentary = form.cleaned_data['commentary']

            html = render_to_string('emails/email.html', {
                'code': code,
                'email': email,
                'name': name,
                'type': type,
                'serial_number': serial_number,
                'item': item_number,
                'date': date,
                'commetary': commentary,
            }
            
            ) 
            send_mail('The contact form sub', 'Message', 'noreply@weg.net', ['koura@mailtrap.io'], html_message=html, fail_silently=False)
            
            return redirect('home')
    else:
        form = Form()
        
    return render(request, 'template.html', {
        'form': form 
    })
