from django.shortcuts import render, redirect
from .forms import Form, Form2
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .component import component_type




def home(request):
    form2 = Form2(request.POST)
    form = Form(request.POST)
    if request.method == 'POST':
        choices = request.POST.get('choices')
        quantity = request.POST.get('quantity')

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

            age = form2.cleaned_data['age']

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
                'quantity': quantity,
                'choices': choices,
                'age': age,
            }           
            )
            send_mail('Kits request', 'Message', 'parts-wmo@weg.net', ['koura@weg.net', email], html_message=html, fail_silently=False)
            return redirect('home')
    else:
        form = Form()
        form2 = Form2()

    return render(request, 'template.html', {
        'form': form,
        'form2':form2,
        'component_type': component_type,
    })
