from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'clerk'
# "{% url 'polls:vote' question.id %}"s
urlpatterns = [
    path('', views.Home, name='Home'),
    path('register',views.register, name='register'),
    path('edit_card',views.editcard, name='edit_card'),
    path('card',views.card, name='card'),
    
]