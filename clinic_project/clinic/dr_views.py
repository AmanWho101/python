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
        registration__registration_date=date
    )
    
    context={
        'patients':patients
    }
    return render(request,'doctor/room.html',context)

@login_required(redirect_field_name="login")
def patient_checked(request):
    date = datetime.date.today()
    dosage = request.POST.get('amount_id')+' ' +request.POST.get('type_id')+' ' +request.POST.get('frequency_id')
    drug_pri = Drug_prescriptions(
        disease_id=request.POST.get('disease_id'),
        drug_id=request.POST.get('drug_id'),
        priscription_id=request.POST.get('priscription_id'),
        quantity=request.POST.get('quantity'),
        dosage=dosage,
        remark=request.POST.get('remark'),
    )
    drug_pri.save()
    examination = Priscriptions.objects.get(id=drug_pri.priscription_id)
    examination.examination_date = date
    examination.save(update_fields=['examination_date'])
    context = {
        'msg': "Change Saved Successfully!"
    }
    return render(request,'doctor/index.html',context)

@login_required(redirect_field_name="login")
def getData(request):
    
    date = datetime.date.today()
    patients = Priscriptions.objects.filter(
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
    categorys_name = Category.objects.get(pk=id)
    drugs = Drugs.objects.filter(category_id=id)
    context = {
        'categorys_name':categorys_name,
        'categorys':categorys,
        'frequencys':frequency,
        'dosage_types':dosage_type,
        'amounts':amount,
        'drugs':drugs,
    }
    return render(request,'doctor/priscription.html',context)