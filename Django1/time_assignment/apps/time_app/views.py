from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>The current time and date: </h1><h3>%s/%s/%s  %s:%s:%s</h3></body></html>" %(now.day, now.month,now.year, now.hour,now.minute, now.second)
    return HttpResponse(html)
