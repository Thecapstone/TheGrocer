from django.urls import path
from . import views
from .views import grocer_login_view, buyer_login_view, grocer_registration_view, buyer_registration_view, index

app_name = "accounts"

urlpatterns = [
    path('', index, name='index'),
    path('register/grocer/', grocer_registration_view, name='register_grocer'),
    path('register/buyer/', views.buyer_registration_view, name='register_buyer'),
    path('login/grocer/', grocer_login_view, name='grocer_login'),
    path('login/buyer/', buyer_login_view, name='buyer_login'),
]