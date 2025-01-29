from django.shortcuts import *
from  django.contrib.auth.decorators import *
from ssms_model.models import *
import datetime
from django.http import JsonResponse

# Create your views here.
@login_required(redirect_field_name="login")
def Home(request):
    return render(request,'reception/index.html')

@login_required(redirect_field_name="login")
def register(request):
    date = datetime.date.today()
    todays_patient = Priscriptions.objects.\
            select_related('student').\
                filter(
                            
                            examination_date__isnull=True,
                            registration__registration_date=date
                               )
    
    doctors = Doctors.objects.all()

    context={
        'patient':todays_patient,
        'doctors':doctors
    }
    
    return render(request,'reception/register.html',context)

@login_required(redirect_field_name="login")
def editcard(request):
    context={}
    return render(request,'reception/card_edit.html',context)

@login_required(redirect_field_name="login")
def card(request):
    context={}
    return render(request,'reception/card.html',context)

@login_required(redirect_field_name="login")
def fetch_data(request):
    context={  
        }
    try:
        data = Students.objects.get(barcode = request.POST.get('data'))
    except:
        context={
            'associate':'Student id should be associated! please use the ⇓ Button to associate.',
            'style':'danger',
            'barcode':request.POST.get('data'),
        }
        return render(request,'reception/associate.html',context)
    else:
        date = datetime.date.today()
        cards_asso = get_object_or_404(Student_cards, student=data.id)
        cards = get_object_or_404(Card, id=cards_asso.card_id)
        years = get_object_or_404(Years, id=data.entry_batch)
        #get free doctors
        doctors = Doctors.objects.all()
        list_doctors = {
        }
        check_prisc = Priscriptions.objects.filter(
            examination_date__isnull=True,
            registration__registration_date=date
        )[0]
        if check_prisc:
            context={
            'data':data,
            'cards':cards,
            'year':years,
            'allready_assigned':'check_prisc.id',
            'msg':'Allready Assigned'
                }
            return render(request,'reception/table.html',context)
        for doc in doctors:
           counts = Priscriptions.objects.\
                filter(
                            doctor_id=doc.id,
                            examination_date__isnull=True,
                            registration__registration_date=date
                               ).\
                                count()
           
           personal_ = Employees.objects.get(pk=doc.employee_id)
           list_doctors[personal_.full_name]=[counts,doc.id]
        context={
            'data':data,
            'cards':cards,
            'year':years,
            'doctors':list_doctors
        }
    return render(request,'reception/table.html',context)

@login_required(redirect_field_name="login")
def associate(request):
    msg = ''
    try:
        data = Students.objects.get(id_number = request.POST.get('code'))
    except  Students.DoesNotExist:
        context={
            'associate':'No student In the Database! Please Ask Help From The Administrator.',
            'style':'danger',
            }
        return render(request,'reception/associate.html',context)
    else:
        date = datetime.date.today()
        regis = Registration(
            registration_date = date,
            student_id=data.id,
            reception_id= request.user.id,  #api data
            employee_id=None
            )
        data.barcode = request.POST.get('code')
        data.save(update_fields=['barcode'])
        ent_batch = str(data.entry_batch)+'-'
        cards = Card.objects.filter(number__startswith=ent_batch).order_by('-number')
        if not cards:
            date = datetime.date.today()
            e_bath = str(data.entry_batch)+'-'+str(1)

            card_done = Card(number=e_bath, location_id=date.year)
            card_done.save()

            stude = Student_cards(
                date=date, 
                card_id=card_done.id, 
                student_id=data.id
                )
            stude.save()
        else:
            card_ = cards[0].number.split('-')
            incr = int(card_[1])+1
            numb = card_[0]+'-'+str(incr)
            date = datetime.date.today()
            
            card_done = Card(number=numb, location_id=date.year)
            card_done.save()


            stude = Student_cards(
                date=date, 
                card_id=card_done.id, 
                student_id=data.id
                )
            stude.save()
        msg = 'Associated successfully.'
    context={
            'success':msg,
            'style':'success',
            }
    return render(request,'reception/associate.html',context)


@login_required(redirect_field_name='login')
def assign_doctor(request):
    doctor_id = request.POST.get('doc_id')
    id_number = request.POST.get('id_number')
    
    register_id = Registration.objects.filter(
        student_id__id_number=id_number
    )[0]
    priscr = Priscriptions(
                            doctor_id=doctor_id, 
                            student_id=register_id.student_id, 
                            registration_id=register_id.id
                            )
    priscr.save()
    context={
            'success':'Doctor Assigned',
            'style':'success',
            }
    return render(request, 'reception/msg.html',context)

@login_required(redirect_field_name="login")
def change_doctor(request):
    doc_id = request.POST.get('doc_id')
    stud_id = request.POST.get('stud_id')
    change_doc_id = request.POST.get('change_doc_id')
    date = datetime.date.today()
    changedoc = Priscriptions.objects.filter(
                            doctor_id=change_doc_id, 
                            student_id=stud_id, 
                            registration__registration_date=date
                            )[0]

    changedoc.doctor_id = doc_id
    changedoc.save(update_fields=['doctor_id'])

    data = {
        'success':"Doctor Changed!"
        }
    return JsonResponse(data)

@login_required(redirect_field_name='login')
def searchID(request):
    idnumber = request.POST.get('id_number')
    student = Students.objects.filter(
        id_number = idnumber
    )
    
    context={'student':None}
    if student:
        student=student[0]
        card = Student_cards.objects.get(student_id=student.id)
        context = {
            'student':student,
            'card':card
            }
    return render(request,'reception/editcard.html',context)

@login_required(redirect_field_name='login')
def updatecard(request):
    number = request.POST.get('number')
    location = request.POST.get('location')
    id = request.POST.get('id')

    card_update = Card.objects.get(pk=id)
    card_update.number=number
    card_update.location_id=location
    card_update.save(update_fields=['number','location_id'])

    data = {
        'success':"Card updated successfully!"
            }
    return JsonResponse(data)