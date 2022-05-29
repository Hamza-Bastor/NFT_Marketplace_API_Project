from django.contrib import admin

from nft.models import Nft, Product, Collection, Account


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'product_description',
                    'product_url', 'img_url', 'collection', 'owner')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ('username', 'address', 'password')


@admin.register(Nft)
class NftAdmin(admin.ModelAdmin):

    list_display = ('photo', 'name', 'description')
