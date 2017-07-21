from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..userdashboard_app.models import User_Level
from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        user=User.objects.register(request.POST)
        if user[0]:
            context={'message': user[1]}
            request.session['user_id']=user[2].id
            request.session['user_level']=User_Level.objects.assignlevel(request.session['user_id'])
            request.session['user_email']=request.POST['email']
            return redirect(reverse('dashboard:board'))
        else:
            context={'errors': user[1]}
            return render(request, 'log_reg_app/register.html', context)
    else:
        return render(request, 'log_reg_app/register.html')

def login(request):
    if request.method == 'POST':
        user=User.objects.login(request.POST)
        if user[0]:
            request.session['user_id']=user[2].id
            request.session['user_email']=user[2].email
            request.session['user_level']=User_Level.objects.get(user_id=request.session['user_id']).level
            context={'message': user[1]}
            return redirect(reverse('dashboard:board'))
        else:
            context={'errors': user[1]}
            return render(request, 'log_reg_app/login.html', context)
    else:
        return render(request, 'log_reg_app/login.html')

def logout(request):
    request.session.pop('user_id')
    request.session.pop('user_email')
    request.session.pop('user_level')
    return redirect(reverse('dashboard:index'))
