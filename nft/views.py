
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import viewsets
from nft.models import Register, Collection, Product
from nft.serializers import RegisterSerializer, CollectionSerializer, ProductSerializer
from .form import RegisterForm
from django.contrib.auth import authenticate, login


# signup part


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signup')
    else:
        form = RegisterForm
    return render(request, 'nft/signup.html', {'form': form})


# signin part
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


class RegisterViewSet(viewsets.ModelViewSet):

    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    search_fields = ['user_name']
