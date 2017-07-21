from django.shortcuts import render, redirect, HttpResponse
import re, bcrypt
from django.core.urlresolvers import reverse
from ..log_reg_app.models import User
from .models import Message, Comment, User_Level, Description
# Create your views here.
def index(request):
    users=User.objects.all()
    for user in users:
        print user.first_name, user.email
    return render(request, 'userdashboard_app/index.html')

def board(request):
    # d=Description.objects.all()
    # print "CCCCCCCC", d.description
    if int(request.session['user_level']) == 9:
        print "ADMIN"
        return redirect(reverse('dashboard:dashboard', kwargs={'level': "admin"}))
    else:
        print "NORMAL"
        return redirect(reverse('dashboard:dashboard', kwargs={'level': ""}))

def dashboard(request, level):
    users=User_Level.objects.all()
    context={'users': users,
    }
    if level=='admin':
        print "admin"
        return render(request, 'userdashboard_app/dashboard_admin.html', context)
    elif level=='':
        print "normal"
        return render(request, 'userdashboard_app/dashboard.html', context)
    else:
        return HttpResponse("No access.")

def add(request):
    return render(request, 'userdashboard_app/add.html')

def new(request):
    user=User.objects.register(request.POST)
    if user[0]:
        User_Level.objects.assignlevel(user[2].id)
        return redirect(reverse('dashboard:board'))
    else:
        context={'errors': user[1]}
        return render(request, 'userdashboard_app/add.html', context)

def profile(request):
    user=User_Level.objects.get(user_id=request.session['user_id'])
    context={'user': user}
    return render(request, 'userdashboard_app/profile.html', context)

def edit(request, id):
    user=User_Level.objects.get(user_id=id)
    context={'user': user }
    return render(request, 'userdashboard_app/edit.html', context)

def update(request, id):
    user=User.objects.filter(id=id)
    if (request.POST['update'] == 'edit_information'):
        user.update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        if 'user_level' in request.POST:
            level=User_Level.objects.filter(user_id=id).update(level=request.POST['user_level'])

    elif (request.POST['update'] == 'change_password'):
        password=request.POST['password']
        v=User.objects.validate_password(request.POST)
        if v[0]:
            user.update(password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()), confirm_password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
        else:
            context={'errors': v[1] }
            print context
            return redirect(reverse('dashboard:edit', kwargs={'id': id}))

    elif (request.POST['update'] == 'edit_description'):
        print "HEREEEEEEEEE"
        print request.POST['description']
        d=Description.objects.filter(user_id=id)
        if d:
            d.update(description=request.POST['description'])
        else:
            d=Description.objects.create(description=request.POST['description'], user=user[0])
    return redirect(reverse('dashboard:board'))

def remove(request, id):
    user=User.objects.get(id=id)
    context={'user': user}
    return render(request, 'userdashboard_app/confirmdeletion.html', context)

def destroy(request, id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect(reverse('dashboard:board'))

def show(request, id):
    user=User.objects.get(id=id)
    messages=Message.objects.filter(receiver=user)
    try:
        d=Description.objects.get(user=user)
    except:
        d={'description': "No description."}
    try:
        c=Comment.objects.all()
    except:
        c={'comments': " "}
    context={
    'user': user,
    'messages': messages,
    'description': d,
    'comments': c
    }
    print request.session['user_email']
    c=Comment.objects.all()
    for a in c:
        print a.comment
    return render(request, 'userdashboard_app/show.html', context)

def addmessage(request, id):
    creator=User.objects.get(id=request.session['user_id'])
    receiver=User.objects.get(id=id)
    message=Message.objects.create(message=request.POST['entered_message'], creator=creator, receiver=receiver)
    return redirect(reverse('dashboard:show', kwargs={'id': id}))

def addcomment(request, id):
    creator=User.objects.get(id=request.session['user_id'])
    message=Message.objects.get(id=id)
    comment=Comment.objects.create(comment=request.POST['entered_comment'], message=message, creator=creator)
    return redirect(reverse('dashboard:show', kwargs={'id': message.receiver.id}))
