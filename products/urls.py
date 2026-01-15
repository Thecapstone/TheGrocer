from django.urls import path
from .views import CreateProductView, ProductsListView, ProductDetailView

app_name = "products"

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('list/', ProductsListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]