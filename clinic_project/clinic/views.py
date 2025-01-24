from django.shortcuts import *
from  django.contrib.auth.decorators import *
from ssms_model.models import *
import datetime

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
        return render(request,'associate.html',context)
    else:
        cards_asso = get_object_or_404(Student_cards, student=data.id)
        cards = get_object_or_404(Card, id=cards_asso.card_id)
        years = get_object_or_404(Years, id=data.entry_batch)
        #get free doctors
        doctors = Doctors.objects.all()
        list_doctors = {

        }
        index=1
        for data in doctors:
            #examination_date not equal None
           counts = Priscriptions.objects.filter(doctor_id=data.id).filter(examination_date=None).count()
           personal_ = Employees.objects.get(pk=data.employee_id)
           list_doctors[personal_.full_name]=counts
        context={
            'data':data,
            'cards':cards,
            'year':years,
            'doctors':list_doctors
        }
    print(context)
    return render(request,'table.html',context)

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
        return render(request,'associate.html',context)
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
            }
    return render(request,'associate.html',context)