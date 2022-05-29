import collections
from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.contrib import admin
# Create your models here.

SEMESTER_CHOICES = (
    ("PandaZ", "PandaZ"),
    ("FoxZ", "FoxZ"),
    ("MonkeyZ", "MonkeyZ"),

)

SEMESTER_CHOICES2 = (
    ("Hamza", "Hamza"),
    ("Aymen", "Aymen"),
)


class Product(models.Model):

    product_name = models.CharField(max_length=20)
    product_description = models.TextField()
    product_url = models.URLField()
    img_url = models.URLField()
    collection = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES)
    owner = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES2)


class Collection(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Account(models.Model):
    username = models.CharField(max_length=20)
    address = models.EmailField()
    password = models.CharField(max_length=30)


class Nft(models.Model):
    photo = models.ImageField(upload_to='')
    name = models.CharField(max_length=20)
    description = models.TextField()
