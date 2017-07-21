from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    users=User.objects.all()
    for u in users:
        print u.name
    return render(request, 'survey_app/index.html')

def create(request):
    context={
    'data': request.POST
    }
    name=User.objects.create(name=request.POST['name'])
    return render(request, 'survey_app/result.html', context)
