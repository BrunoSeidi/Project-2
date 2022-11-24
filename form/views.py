from django.shortcuts import render, redirect
from .forms import Form
from django.core.mail import send_mail
from django.template.loader import render_to_string


def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
 
        if form.is_valid():
            name = form.cleaned_data['name']
            branchName = form.cleaned_data['branchName']
            email = form.cleaned_data['email']
            
            type = form.cleaned_data['type']
            number = form.cleaned_data['number']
            date = form.cleaned_data['date']
            phase = form.cleaned_data['phase']
            capacity = form.cleaned_data['capacity']
            centerQuantity = form.cleaned_data['centerQuantity']
            componentQuantity = form.cleaned_data['componentQuantity']
            componentSelection = form.cleaned_data['componentSelection']
            commentary = form.cleaned_data['commentary']
            # componentQuantity1 = form.cleaned_data['componentQuantity1']
            # componentSelection1 = form.cleaned_data['componentSelection1']
            # componentQuantity2 = form.cleaned_data['componentQuantity2']
            # componentSelection2 = form.cleaned_data['componentSelection2']
            # componentQuantity3 = form.cleaned_data['componentQuantity3']
            # componentSelection3 = form.cleaned_data['componentSelection3']
            # componentQuantity4 = form.cleaned_data['componentQuantity4']
            # componentSelection4 = form.cleaned_data['componentSelection4']
            
            html = render_to_string('emails/email.html', {
                'name': name,
                'branchName': branchName,
                'email': email,
                'type': type,
                'number': number,
                'date': date,
                'phase': phase,
                'capacity': capacity,
                'centerQuantity': centerQuantity,
                'componentQuantity': componentQuantity,
                'componentSelection': componentSelection,
                'commentary': commentary,
            }           
            )
            send_mail('Kits request', 'Message', 'parts-wmo@weg.net', ['koura@weg.net', email], html_message=html, fail_silently=False)
            
            return redirect('home')
    else:
        form = Form()
        
    return render(request, 'template.html', {
        'form': form
    })
