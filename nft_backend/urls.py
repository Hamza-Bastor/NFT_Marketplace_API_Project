"""nft_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.db import router
from django.urls import include, path
from rest_framework import routers
from nft.urls import router as nft_router
from nft import views


router = routers.DefaultRouter()
router.registry.extend(nft_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('rest/', include(router.urls)),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', views.users),
    path('add_user', views.add_user, name="add_user"),
    path('delete_user/<int:myid>/', views.delete_user, name="delete_user"),
    path('edit_user/<int:myid>/', views.edit_user, name="edit_user"),
    path('update_user/<int:myid>/', views.update_user, name="update_user"),
    path('products/', views.products),
    path('add_product', views.add_product, name="add_product"),
    path('delete_product/<int:myid>/',
         views.delete_product, name="delete_product"),
    path('edit_product/<int:myid>/', views.edit_product, name="edit_product"),
    path('update_product/<int:myid>/',
         views.update_product, name="update_product"),
    path('nfts/', views.nfts),
    path('add_nft', views.add_nft, name="add_nft"),
    path('nfts/', views.nfts),
    path('profils/', views.profil),
]
