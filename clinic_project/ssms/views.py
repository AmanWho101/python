from django.shortcuts import *
from  django.contrib.auth.decorators import *

@login_required(redirect_field_name="login")
def auth(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin'):
            return redirect('/admin/')
        elif request.user.groups.filter(name='reception'):
            return redirect('/clinic/reception/home')
        
        elif request.user.groups.filter(name='doctor'):
            return redirect('/clinic/doctor/home')
        else:
            return HttpResponse('<h1>user has no group</h1>')
        