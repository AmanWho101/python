from django.db import models

# Create your models here.

class Statuses(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

class Active_statuses(models.Model):
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    active = models.IntegerField(blank=True, null=True)

class Admission_fields(models.Model):
    name = models.CharField(max_length = 200)

class Admission_types(models.Model):
    name = models.CharField(max_length = 200)
    accronym = models.CharField(max_length = 200)

class Amount(models.Model):
    name = models.CharField(max_length = 200)

class Card(models.Model):
    number = models.CharField(blank=True, null=True,max_length = 200)
    location_id = models.IntegerField(blank=True, null=True)
#need checking
class Category(models.Model):
    name = models.CharField(max_length = 200)

class Degrees(models.Model):
    name = models.CharField(max_length = 200)
    accronym = models.CharField(max_length = 200)

class Schools(models.Model):
    name = models.CharField(max_length = 200)

class Departments(models.Model):
    name = models.CharField(max_length = 200)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

class Disabilities(models.Model):
    name  = models.CharField(max_length = 200)

class Diseases(models.Model):
    name = models.CharField(max_length = 200)
    diseases_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length = 200)

class Doctors(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class Dosage_type(models.Model):
    name = models.CharField(max_length = 200)

class Drugs(models.Model):
    name = models.CharField(max_length = 200)
    unit = models.CharField(max_length = 200)
    quantity = models.IntegerField(blank=True, null=True)
    unit_price = models.CharField(max_length = 200)
    manufacturer = models.CharField(max_length = 200)
    batch_number = models.CharField(max_length = 200)
    expire_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Drug_infos(models.Model):
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    unit_price = models.CharField(max_length = 200)
    quantity = models.IntegerField(blank=True, null=True)
    received_date = models.DateField()

class Pharmacists(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class Pharmacy(models.Model):
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    pharmacists = models.ForeignKey(Pharmacists, on_delete=models.CASCADE)


class Drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date = models.DateTimeField()
    received_date = models.DateTimeField()
    requested_by = models.IntegerField(blank=True, null=True) 
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

class Employee_cards(models.Model):
    employee_id = models.IntegerField(blank=True, null=True) # api person id
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)

class Examination_catagory(models.Model):
    name = models.CharField(max_length = 200)

class Examination_subcatagory(models.Model):
    name  = models.CharField(max_length = 200)
    examination_catagory = models.ForeignKey(Examination_catagory, on_delete=models.CASCADE)

class Examination_type(models.Model):
    name = models.CharField(max_length = 200)
    examination_subcatagory = models.ForeignKey(Examination_subcatagory, on_delete=models.CASCADE)

class Examination_type_options(models.Model):
    examination_type = models.ForeignKey(Examination_type, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)

class Frequency(models.Model):
    name = models.CharField(max_length = 200)

class Gender(models.Model):
    name = models.CharField(max_length = 200)

class Lab_technicians(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class Laboratories(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    remark = models.TextField(max_length = 200)
    lab_technician = models.ForeignKey(Lab_technicians, on_delete=models.CASCADE)

class Lab_drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date = models.DateField()
    received_date = models.DateField()
    requested_by = models.IntegerField(blank=True, null=True) 
    laboratory = models.ForeignKey(Laboratories, on_delete=models.CASCADE)

class Nurses(models.Model):
    employee_id = models.IntegerField(blank=True, null=True) # api person id

class OPD(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    remark = models.TextField()
    nurse = models.ForeignKey(Nurses, on_delete=models.CASCADE)

class OPD_drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date= models.DateField() 
    received_date= models.DateField() 
    requested_by = models.IntegerField(blank=True, null=True)
    opd = models.ForeignKey(OPD, on_delete=models.CASCADE)

class Students(models.Model):
    personal_name = models.CharField(max_length = 200)
    father_name = models.CharField(max_length = 200)
    grand_father_name = models.CharField(max_length = 200)
    id_number = models.CharField(max_length = 200)
    exam_registration_no = models.CharField(max_length = 200)
    barcode = models.CharField(max_length = 200)
    entry_batch = models.IntegerField(blank=True, null=True)
    current_batch = models.IntegerField(blank=True, null=True)
    admission_field = models.ForeignKey(Admission_fields, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    disability = models.ForeignKey(Disabilities, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degrees, on_delete=models.CASCADE)
    admission_type = models.ForeignKey(Admission_types, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length = 200)
    manuplator_id = models.IntegerField(blank=True, null=True)
    archived = models.IntegerField(blank=True, null=True)


class Employees(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    work_unit = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)


class Pending_id_prints(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE) # api student id
    employee_id = models.IntegerField(blank=True, null=True) # api person id

class Reception(models.Model):
    employee_id = models.IntegerField(blank=True, null=True) # api person id

class Refer_types(models.Model):
    name = models.CharField(max_length = 200)

class Registration(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    reception = models.ForeignKey(Reception, on_delete=models.CASCADE)
    employee_id = models.IntegerField(blank=True, null=True) # api person id

class Settings(models.Model):
    propertys = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)

class Student_cards(models.Model):
    date = models.DateField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

class Tesme(models.Model):
    drug = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    pharmasist = models.ForeignKey(Pharmacists, on_delete=models.CASCADE)

class Years(models.Model):
    name = models.IntegerField(blank=True, null=True)

class Priscriptions(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    examination_date = models.DateTimeField(auto_now_add=True)
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    employee_id = models.IntegerField(blank=True, null=True)

class Refers(models.Model):
    refer_type = models.ForeignKey(Refer_types, on_delete=models.CASCADE)
    priscription = models.ForeignKey(Priscriptions, on_delete=models.CASCADE)
    remark = models.CharField(max_length = 200)

class Lab_examination(models.Model):
    priscription = models.ForeignKey(Priscriptions, on_delete=models.CASCADE)
    lab_technicians = models.ForeignKey(Lab_technicians, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    status = models.IntegerField(blank=True, null=True) 
    examination_type = models.ForeignKey(Examination_type, on_delete=models.CASCADE)
    request_date = models.DateField()
    result = models.CharField(max_length = 200) 
    result_date = models.DateField()
    remark = models.CharField(max_length = 200) 

class Drug_prescriptions(models.Model):
    disease  = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    drug  = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    priscription = models.ForeignKey(Priscriptions, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length = 200)
    student_signature = models.CharField(max_length = 200)
    delivery_date = models.DateTimeField()
    pharmasist = models.ForeignKey(Pharmacists, on_delete=models.CASCADE)
    remark = models.CharField(max_length = 200)

