from django.contrib import admin
from shop.models import Category, Product, Order
from utils.price import price_uah


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_price', 'category', 'short_desc']
    search_fields = ['name']
    autocomplete_fields = ['category']

    def get_price(self, product: Product):
        return price_uah(product.price)

    get_price.short_description = 'Price'
    get_price.admin_order_field = 'price'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'get_price', 'delivery_status']
    autocomplete_fields = ['product']

    def get_price(self, obj: Order):
        return price_uah(obj.product.price)

    get_price.short_description = 'Price'
    get_price.admin_order_field = 'price'
