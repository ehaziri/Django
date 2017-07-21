from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'ninjas': "hidden",
    'teksti': "showed",
    'specific': "hidden"
    }
    return render(request, 'disninjas/index.html', context)

def ninja(request, color):
    if not color:
        context = {
        'ninjas': "showed",
        'teksti': "hidden",
        'specific': "hidden"
        }
    else:
        context = {
        'ninjas': "hidden",
        'teksti': "hidden",
        'specific': "showed"
        }
        if color == "blue":
            context.update({'imazhi': "donatello"})
            print "blue"
            print context['imazhi']
        elif color == "orange":
            context.update({'imazhi': "michelangelo"})
        elif color == "red":
            context.update({'imazhi': "raphael"})
        elif color == "purple":
            context.update({'imazhi': "leonardo"})
        else:
            context.update({'imazhi': "notapril"})
    return render(request, 'disninjas/index.html', context)
