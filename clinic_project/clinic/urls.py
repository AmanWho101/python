from django.contrib import admin
from django.urls import path, include
from . import views, dr_views

app_name = 'clinic'
# "{% url 'polls:vote' question.id %}"s change_doctor
urlpatterns = [
    # reception url
    path('reception/home', views.Home, name='Reception_Home'),
    path('reception/register',views.register, name='register'),
    path('reception/edit_card',views.editcard, name='edit_card'),
    path('reception/card',views.card, name='card'),
    path('reception/fetch_data',views.fetch_data, name='fetch_data'),
    path('reception/associate',views.associate, name='associate'),
    path('reception/assign_doctor',views.assign_doctor,name='assign_doctor'),
    path('reception/change_doctor',views.change_doctor,name='change_doctor'),
    path('reception/searchID',views.searchID,name='searchID'),
    path('reception/updatecard',views.updatecard,name='updatecard'),
    # doctor url
    path('doctor/home',dr_views.home,name='doctor_home'),
    path('doctor/room',dr_views.room,name='room'),
    path('doctor/checked',dr_views.patient_checked,name="p_checked"),
    path('doctor/getData',dr_views.getData,name="getData"),
    path('doctor/getPData',dr_views.getPData,name='getPData'),
    # getDrug
    path('doctor/getDrug',dr_views.getDrug,name='getDrug'),

]