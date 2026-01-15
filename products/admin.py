from django.contrib import admin
from .views import CreateProductView, ProductsListView, ProductDetailView
from .models import Product
# Register your models here.

admin.site.register(Product)
admin.site.add_action(CreateProductView)
admin.site.add_action(ProductsListView)
admin.site.add_action(ProductDetailView)