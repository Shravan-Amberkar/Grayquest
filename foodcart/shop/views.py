from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
import time

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # params = { 'no_of_slides':nSlides, 'range' : range(1,nSlides),'product' : products}
    # allProds = [[products, range(1,nSlides), nSlides],
    #             [products, range(1,nSlides), nSlides]]
    allProds = []
    catprods = Product.objects.values('category' , 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds' : allProds}

    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def veg(request):
    product = Product.objects.filter(category = 'Veg')
    return render(request, 'shop/veg.html', {'product':product})

def nonveg(request):
    product = Product.objects.filter(category = 'Non-veg')
    return render(request, 'shop/nonveg.html', {'product':product})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        desc = request.POST.get('desc', "")
        contact = Contact(name=name, email = email, phone = phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})
