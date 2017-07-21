from django.shortcuts import render
import random

# Create your views here.
def index(request):
    request.session['money'] = 0
    return render(request, "gold/index.html")

def process(request):
    context={
    'teksti': ""
    }
    if(request.POST['building'] == 'farm'):
        rand = random.randrange(10,21)
        print rand
        request.session['money'] += rand
        request.session['farm'] = rand
        context.update({'teksti': "Earned " + str(request.session['farm']) + " golds from the farm."})

    elif(request.POST['building'] == 'cave'):
        rand = random.randrange(5,11)
        print rand
        request.session['money'] += rand
        request.session['cave'] = rand
        context.update({'teksti': "Earned " + str(request.session['cave']) + " golds from the cave."})

    elif(request.POST['building'] == 'house'):
        rand = random.randrange(2,6)
        print rand
        request.session['money'] += rand
        request.session['house'] = rand
        context.update({'teksti': "Earned " + str(request.session['house']) + " golds from the house."})

    elif(request.POST['building'] == 'casino'):
        rand = random.randrange(0,51)
        print rand
        request.session['money'] -= rand
        request.session['casino'] = rand
        context.update({'teksti': "Entered a casino and lost " + str(request.session['casino']) + " golds."})

    return render(request, 'gold/index.html', context)
