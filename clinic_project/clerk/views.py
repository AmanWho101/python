from django.shortcuts import render
from  django.contrib.auth.decorators import *

# Create your views here.
@login_required(redirect_field_name="login")
def Home(request):
    return render(request,'index.html')

@login_required(redirect_field_name="login")
def register(request):
    context={}
    return render(request,'register.html',context)

@login_required(redirect_field_name="login")
def editcard(request):
    context={}
    return render(request,'card_edit.html',context)

@login_required(redirect_field_name="login")
def card(request):
    context={}
    return render(request,'card.html',context)