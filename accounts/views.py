from django.shortcuts import redirect, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from .forms import GrocerRegistrationForm, BuyerRegistrationForm, GrocerLoginForm, BuyerLoginForm


# Create your views here.
def index(request):
    template ='accounts/index.html'
    return render(request, template)


def grocer_registration_view(request):
    if request.method == 'POST':
        form = GrocerRegistrationForm(request.POST)
        if form.is_valid():
            # Save your data here
            return redirect('accounts:grocer_login')
    else:
        form = GrocerRegistrationForm()
    
    return render(request, 'accounts/grocersignup.html', {'form': form})

def grocer_login_view(request):
    if request.method == 'POST':
        form = GrocerLoginForm(request.POST)
        if form.is_valid():
            # Authenticate your user here
            return redirect('products:create-product')
    else:
        form = GrocerLoginForm()
    
    return render(request, 'accounts/grocerlogin.html', {'form': form})
        

def buyer_registration_view(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            # Save your data here
            return redirect('accounts:buyer_login')
    else:
        form = BuyerRegistrationForm()
    
    return render(request, 'accounts/buyersignup.html', {'form': form})

def buyer_login_view(request):
    if request.method == 'POST':
        form = BuyerLoginForm(request.POST)
        if form.is_valid():
            # Authenticate your user here
            return redirect('products:list')
    else:
        form = BuyerLoginForm()
    
    return render(request, 'accounts/buyerlogin.html', {'form': form})
    