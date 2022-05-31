from itertools import product
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from nft.models import Account, Collection, Product, Nft
from nft.serializers import AccountSerializer, CollectionSerializer, ProductSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignupForm, UserCreationForm


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


# user page
def users(request):
    user_list = Account.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'nft/users.html', context)


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


# home page
def home(request):
    return render(request, 'nft/home.html', {})


# signup page
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful!")
                return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'authenticate/signup.html', {'form': form})


# signin page
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome Back!")
            return redirect('home')
        else:
            return redirect('signin')

    else:
        return render(request, 'authenticate/signin.html', {})


# sign out
def signout(request):
    logout(request)
    return redirect('home')


# profil
def profil(request):
    return render(request, 'nft/profils.html', {})


# nft page
def nfts(request):
    return render(request, 'nft/nfts.html', {})


# add nft
def add_nft(request):
    if request.method == "POST":
        photo = request.POST['photo']
        name = request.POST['name']
        description = request.POST['description']
        nft = Nft(photo=photo, name=name,
                  description=description)
        nft.save()
        messages.info(request, "NFT ADDED SUCCESSFULLY")
    return render(request, 'nft/nfts.html', {})


# create ViewSet class
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
