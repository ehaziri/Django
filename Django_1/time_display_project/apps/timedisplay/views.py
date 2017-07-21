from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.

def index(request):
    date = datetime.datetime.now()
    context = {
    "currentdate": date
    }
    return render(request, 'appname/page.html', context)
