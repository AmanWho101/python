from django.shortcuts import *
from  django.contrib.auth.decorators import *
from ssms_model.models import *
import datetime
from django.http import JsonResponse

@login_required(redirect_field_name="login")
def home(request):
    context={}
    return render(request,'doctor/index.html',context)

@login_required(redirect_field_name="login")
def room(request):
    context={}
    return render(request,'doctor/room.html',context)