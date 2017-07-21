from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    for p in products:
        print p.id, p.name, p.description, p.price
    context={'products': products}
    return render(request, 'semirestfulroutes_app/index.html', context)

def new(request):
    return render(request, 'semirestfulroutes_app/new.html')

def create(request):
    product=Product.objects.create(name=request.POST['name'],
    description=request.POST['description'], price=request.POST['price'])
    product.save()
    return redirect('/')

def show(request, id):
    product=Product.objects.get(id=id)
    context={'product': product}
    return render(request, 'semirestfulroutes_app/show.html', context)

def edit(request, id):
    product=Product.objects.get(id=id)
    context={'product': product}
    return render(request, 'semirestfulroutes_app/edit.html', context)

def update(request, id):
    product=Product.objects.get(id=id)
    updated=Product.objects.filter(id=id).update(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    # updated.save()
    return redirect('/')

def destroy(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('/')
