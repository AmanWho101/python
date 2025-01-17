from django.shortcuts import *

def auth(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin'):
            return redirect('/admin/')
        elif request.user.groups.filter(name='receptions'):
            return redirect('/reception/')
        