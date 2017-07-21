from django.shortcuts import render,redirect, HttpResponse
import random, string
# Create your views here.
def index(request):
    if not 'how_many_times' in request.session:
        request.session['how_many_times']=0
        request.session['random_string'] = 'Click Generate Button for a Random String'
    return render(request, 'randomstring_app/index.html')

def generate(request):
    request.session['how_many_times']= request.session['how_many_times'] + 1
    rand = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(16)])
    request.session['random_string']=rand
    return redirect('/')

def reset(request):
    del request.session['how_many_times']
    del request.session['random_string']
    return redirect('/')
