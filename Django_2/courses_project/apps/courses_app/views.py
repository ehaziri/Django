from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Course, Comment

# Create your views here.
def index(request):
    courses=Course.objects.all()
    context={'courses': courses}
    return render(request, 'courses_app/index.html', context)

def create(request):
    result=Course.objects.register(request.POST)
    if result != "":
        messages.error(request, result)
    return redirect(reverse('index'))

def remove(request, id):
    course=Course.objects.get(id=id)
    context={'course': course}
    return render(request, 'courses_app/confirmation.html', context)

def destroy(request, id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect(reverse('index'))

def show(request, id):
    try:
        comments=Comment.objects.all()
        for c in comments:
            print "^^^", c.comment
    except:
        pass
    course=Course.objects.get(id=id)
    context={'course': course}
    return render(request, 'courses_app/add_show_comments.html', context)

def add(request, id):
    course=Course.objects.get(id=id)
    comment=Comment.objects.create(comment=request.POST['comment'], course=course)
    return redirect(reverse('show', kwargs={'id': id}))


def remove_comment(request, id):
    comment=Comment.objects.get(id=id)
    comment.delete()
    return redirect(reverse('show', kwargs={'id': comment.course.id}))
