from django.contrib import admin

from nft.models import Product, Collection, Register


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_name', 'product_description',
                    'product_url', 'img_url', 'collection', 'owner')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    list_display = ('name', 'collection_url')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):

    list_display = ('username', 'address', 'password')
