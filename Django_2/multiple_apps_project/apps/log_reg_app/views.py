from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import date
from .models import User
# Create your views here.
def index(request):
    print date.today()
    try:
        users=User.objects.all()
        for u in users:
            print u.email, u.password
        print "user_name session: ", request.session['user']['first_name']
    except:
        pass
    return render(request, 'log_reg_app/index.html', context={'today': date.today()})

def register(request):
    user=User.objects.register(request.POST)
    if user[0] == False:
        for message in user[1]:
            messages.error(request, message)
        return redirect(reverse('index'))
    messages.success(request, "Welcome, {}! You were successfully registered.".format(user[1].first_name))
    return log_user_in(request, user[1])

def login(request):
    user=User.objects.login(request.POST)
    if user[0] == False:
        for message in user[1]:
            messages.error(request, message)
        return redirect(reverse('index'))
    messages.success(request, "Welcome, {}! You were successfully logged in.".format(user[1].first_name))
    return log_user_in(request, user[1])

def success(request):
    if check_user_logged_in(request) == True:
        return redirect(reverse('courses_users:index'))
    else:
        return redirect(reverse('users:index'))

def log_user_in(request, user):
    request.session['user']={
    'id': user.id,
    'first_name': user.first_name,
    'last_name': user.last_name,
    'email': user.email,
    }
    #REDIRECT TO APP instead!
    return redirect(reverse('users:success'))

def logout(request):
    request.session.pop('user')
    return redirect(reverse('users:index'))

def check_user_logged_in(request):
    if 'user' in request.session:
        return True
    else:
        return False
