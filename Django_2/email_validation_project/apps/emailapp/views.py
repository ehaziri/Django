from django.shortcuts import render, redirect
from .models import Email
# Create your views here.

def index(request):
    context={
    'display': 'hide'
    }
    return render(request, 'emailapp/index.html', context)

def register(request):
    valid_email=Email.objects.register(request.POST['email_address'])
    if valid_email[0]:
        request.session['email']=request.POST['email_address']
        return redirect('/successpage')
    else:
        context={
        'display': 'show',
        'error_message': valid_email[1]
        }
        return render(request, 'emailapp/index.html', context)

def successpage(request):
    all_emails=Email.objects.all()
    context={
    'all_emails': all_emails
    }
    return render(request, 'emailapp/success.html', context)
def delete(request, id):
    email=Email.objects.get(id=id)
    email.delete()
    return redirect('/successpage')
