from email.headerregistry import Address
from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from nft.models import Account, Collection, Product
from nft.serializers import AccountSerializer, CollectionSerializer, ProductSerializer
from .form import AccountForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from nft import form

# product page


def products(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request, 'nft/products.html', context)

# adding product


def add_product(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        product_url = request.POST['product_url']
        img_url = request.POST['img_url']
        collection = request.POST['collection']
        owner = request.POST['owner']
        product = Product(product_name=product_name,
                          product_description=product_description, product_url=product_url, img_url=img_url, collection=collection, owner=owner)
        product.save()
        messages.info(request, "PRODUCT ADDED SUCCESSFULLY")
    else:
        pass
    product_list = Product.objects.all()
    context = {
        'product_list': product_list
    }
    return render(request, 'nft/products.html', context)

# delete product


def delete_product(request, myid):
    product = Product.objects.get(id=myid)
    product.delete()
    messages.info(request, "PRODUCT DELETED SUCCESSFULLY")
    return redirect(products)

# edit product


def edit_product(request, myid):
    sel_product = Product.objects.get(id=myid)
    product_list = Product.objects.all()
    context = {
        'sel_product': sel_product,
        'user_list': product_list
    }
    return render(request, 'nft/products.html', context)

# update product


def update_product(request, myid):
    product = Product.objects.get(id=myid)
    product.product_name = request.POST['product_name']
    product.product_description = request.POST['product_description']
    product.product_url = request.POST['product_url']
    product.img_url = request.POST['img_url']
    product.collection = request.POST['collection']
    product.owner = request.POST['owner']
    product.save()
    messages.info(request, "PRODUCT UPDATED SUCCESSFULLY")
    return redirect(products)

# adding user


def add_user(request):
    if request.method == "POST":
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        account = Account(username=username,
                          address=address, password=password)
        account.save()
        messages.info(request, "USER ADDED SUCCESSFULLY")
    else:
        pass
    user_list = Account.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'nft/users.html', context)

# delete user


def delete_user(request, myid):
    account = Account.objects.get(id=myid)
    account.delete()
    messages.info(request, "USER DELETED SUCCESSFULLY")
    return redirect(users)

# edit user


def edit_user(request, myid):
    sel_account = Account.objects.get(id=myid)
    user_list = Account.objects.all()
    context = {
        'sel_account': sel_account,
        'user_list': user_list
    }
    return render(request, 'nft/users.html', context)

# update user


def update_user(request, myid):
    account = Account.objects.get(id=myid)
    account.username = request.POST['username']
    account.address = request.POST['address']
    account.password = request.POST['password']
    account.save()
    messages.info(request, "USER UPDATED SUCCESSFULLY")
    return redirect(users)

# user page


def users(request):
    user_list = Account.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'nft/users.html', context)


# signup page
def signup(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup')
    else:
        form = AccountForm
    return render(request, 'nft/signup.html', {'form': form})


# signin page
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('signup')
        else:
            return redirect('signin')

    else:
        return render(request, 'nft/signin.html', {})


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['collection', 'owner']
    search_fields = ['product_name']


class CollectionViewSet(viewsets.ModelViewSet):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    search_fields = ['name']


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    search_fields = ['user_name']
