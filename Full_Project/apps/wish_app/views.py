from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Wish, Item
from ..log_reg_app.models import User

# Create your views here.
def index(request):
    if check_user_logged_in(request) == True:
        ws=Wish.objects.all()
        for w in ws:
            print "WISHES:", w.item.name, w.user.username

        items=Item.objects.all()
        print "----------------------"
        for i in items:
            print "Items: ", i.name, i.creator.username

        user=User.objects.get(id=request.session['user']['id'])
        wishes=Wish.objects.filter(user=user)
        # items=Item.objects.filter(item_wishes__user=user)
        # others_wishes=Wish.objects.all().exclude(item__in=items)
        others_wishes=Item.objects.exclude(item_wishes__user=user)

        context={
        'wishes': wishes,
        'others_wishes': others_wishes,
        }

        return render(request, "wish_app/index.html", context)
    else:
        return redirect(reverse('users:index'))

def create(request):
    if check_user_logged_in(request) == True:
        return render(request, 'wish_app/add.html')
    else:
        return redirect(reverse('users:index'))

def add(request):
    if check_user_logged_in(request) == True:
        item=Item.objects.add_item(request.POST, request.session['user']['id'])
        if item[0] == False:
            messages.error(request, item[1])
            return redirect(reverse('wish:create'))
        else:
            wish=Wish.objects.add_wish(item[1].id, item[1].creator.id)
            return redirect(reverse('wish:index'))

    else:
        return redirect(reverse('users:index'))

def add_wish(request, id):
    if check_user_logged_in(request) == True:
        wish=Wish.objects.add_wish(id, request.session['user']['id'])
        return redirect(reverse('wish:index'))

    else:
        return redirect(reverse('users:index'))

def show_item(request, id):
    if check_user_logged_in(request) == True:
        item=Item.objects.get(id=id)
        context={
        'item': item
        }
        return render(request, 'wish_app/show.html', context)

    else:
        return redirect(reverse('users:index'))

def delete(request,id):
    if check_user_logged_in(request) == True:
        item=Item.objects.get(id=id)
        item.delete()
        return redirect(reverse('wish:index'))

    else:
        return redirect(reverse('users:index'))

def remove_wish(request,id):
    if check_user_logged_in(request) == True:
        wish=Wish.objects.get(id=id)
        wish.delete()
        return redirect(reverse('wish:index'))

    else:
        return redirect(reverse('users:index'))



def check_user_logged_in(request):
    if 'user' in request.session:
        return True
    else:
        return False
