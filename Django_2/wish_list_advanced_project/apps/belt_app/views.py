from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..wish_app.models import Wish
from ..log_reg_app.models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello belt, you should type /main after localhost to enter.")
