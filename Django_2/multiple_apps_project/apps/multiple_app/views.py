from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..courses_app.models import Course
from ..log_reg_app.models import User

# Create your views here.
def index(request):
    courses=Course.objects.all()
    users=User.objects.all()
    context={
    'users': users,
    'courses': courses,
    }
    return render(request, 'multiple_app/index.html', context)

def create(request):
    add=Course.objects.add_user_to_course(request.POST)
    if add[0] == False:
        messages.error(request, add[1])
    return redirect(reverse('courses_users:index'))
