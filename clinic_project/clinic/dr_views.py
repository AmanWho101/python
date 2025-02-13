from django.shortcuts import *
from  django.contrib.auth.decorators import *
from ssms_model.models import *
import datetime
from django.http import JsonResponse
import datetime

@login_required(redirect_field_name="login")
def home(request):
    context={}
    return render(request,'doctor/index.html',context)

@login_required(redirect_field_name="login")
def room(request):
    date = datetime.date.today()
    patients = Priscriptions.objects.filter(
        examination_date__isnull=True,
        registration__registration_date=date
    )
    context={
        'patients':patients
    }
    return render(request,'doctor/room.html',context)

@login_required(redirect_field_name="login")
def patient_checked(request):
    context = {
        'msg': "Change Saved Successfully!"
    }
    return render(request,'doctor/index.html',context)

@login_required(redirect_field_name="login")
def getData(request):
    
    date = datetime.date.today()
    patients = Priscriptions.objects.filter(
        examination_date__isnull=True,
        registration__registration_date=date,
        student_id=request.POST.get('id')

    )[0]
    diseases = Diseases.objects.all()
    context = {
        'patients': patients,
        'diseases':diseases
    }
    return render(request,'doctor/patientinfo.html',context) 

@login_required(redirect_field_name="login")
def getPData(request):
    categorys = Category.objects.all()
    
    context = {
        'categorys':categorys,
        
    }
    return render(request,'doctor/priscription.html',context) 

@login_required(redirect_field_name="login")
def getDrug(request):
    categorys = Category.objects.all()
    frequency = Frequency.objects.all()
    dosage_type = Dosage_type.objects.all()
    amount = Amount.objects.all()
    id = request.POST.get('id')
    context = {
        'id':request.POST.get('id'),
        'categorys':categorys,
        'frequencys':frequency,
        'dosage_types':dosage_type,
        'amounts':amount,
    }
    print(context)
    return render(request,'doctor/priscription.html',context)