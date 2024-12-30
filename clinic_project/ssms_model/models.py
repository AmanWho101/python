from django.db import models

# Create your models here.
class Active_statuses(models.Model):
    status_id = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

class Admission_fields(models.Model):
    name = models.CharField(max_length = 200)

class Admission_types(models.Model):
    name = models.CharField(max_length = 200)
    accronym = models.CharField(max_length = 200)

class Amount(models.Model):
    name = models.CharField(max_length = 200)

class Api(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

class Blocks(models.Model):
    building_number = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    gender_id = models.IntegerField(blank=True, null=True)
    quality_threshold = models.IntegerField(blank=True, null=True)

class Cafeterias(models.Model):
    name = models.IntegerField(blank=True, null=True)
    accomodation = models.IntegerField(blank=True, null=True)
    accomodation_at_time = models.IntegerField(blank=True, null=True)

class Cafeteria_heads(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)

class Cafeteria_placements(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)
    year_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

class Cafeteria_tickers(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)

class Card(models.Model):
    number = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)

class Card(models.Model):
    name = models.CharField(max_length = 200)

class Ci_sessions(models.Model):
    session_id = models.CharField(max_length = 200)
    ip_address = models.CharField(max_length = 200)
    user_agent = models.CharField(max_length = 200)
    last_activity  = models.IntegerField(blank=True, null=True)
    user_data = models.TextField()

class cs_coordinators(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)

class cs_inventory(models.Model):
    cs_item_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)
    
class cs_items(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    quantity = models.IntegerField(blank=True, null=True)
    unit_price = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    modification = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    expire_date = models.DateField()
    cs_item_category_id = models.IntegerField(blank=True, null=True)

class cs_item_category(models.Model):
    name = models.CharField(max_length = 200)

class cs_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date = models.DateTimeField()
    received_date = models.DateTimeField()
    requested_by = models.IntegerField(blank=True, null=True)
    requester_supervisor = models.IntegerField(blank=True, null=True)
    property_admin = models.IntegerField(blank=True, null=True)
    cs_inventory_id = models.IntegerField(blank=True, null=True)

class cs_shifts(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    cafeteria_id = models.IntegerField(blank=True, null=True)

class data_recorders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    current_batch_id = models.IntegerField(blank=True, null=True)
    admission_fields_id = models.IntegerField(blank=True, null=True)
    admission_type_id = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    start_alphabet = models.CharField(max_length=200)
    end_alphabet = models.CharField(max_length=200)

class degrees(models.Model):
    name = models.CharField(max_length = 200)
    accronym = models.CharField(max_length = 200)

class departments(models.Model):
    name = models.CharField(max_length = 200)
    school_id = models.IntegerField(blank=True, null=True)

class disabilities(models.Model):
    name  = models.CharField(max_length = 200)

class diseases(models.Model):
    name = models.CharField(max_length = 200)
    diseases_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length = 200)

class doctors(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class dormitories(models.Model):
    dormitory_number = models.IntegerField(blank=True, null=True)
    number_of_beds = models.IntegerField(blank=True, null=True)
    reserved_beds = models.IntegerField(blank=True, null=True)
    floor_id = models.IntegerField(blank=True, null=True)
    block_id = models.IntegerField(blank=True, null=True)

class dosage_type(models.Model):
    name = models.CharField(max_length = 200)

class downloads(models.Model):
    name = models.CharField(max_length = 200)
    path = models.CharField(max_length = 200)
    upload_by = models.CharField(max_length = 200)
    upload_time = models.DateTimeField(auto_now_add=True)
    employee_id = models.IntegerField(blank=True, null=True)

class drugs(models.Model):
    name = models.CharField(max_length = 200)
    unit = models.CharField(max_length = 200)
    quantity = models.IntegerField(blank=True, null=True)
    unit_price = models.CharField(max_length = 200)
    manufacturer = models.CharField(max_length = 200)
    batch_number = models.CharField(max_length = 200)
    expire_date = models.DateField()
    category_id = models.IntegerField(blank=True, null=True)

class drug_infos(models.Model):
    drug_id = models.IntegerField(blank=True, null=True)
    unit_price = models.CharField(max_length = 200)
    quantity = models.IntegerField(blank=True, null=True)
    received_date = models.DateField()

class drug_prescriptions(models.Model):
    disease_id  = models.IntegerField(blank=True, null=True)
    drug_id  = models.IntegerField(blank=True, null=True)
    priscription_id  = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length = 200)
    student_signature = models.CharField(max_length = 200)
    delivery_date = models.DateTimeField()
    pharmasist_id  = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length = 200)

class drug_purchase_requests(models.Model):
    drug_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    requested_by = models.IntegerField(blank=True, null=True)
    received_date = models.DateTimeField()
    approved_by = models.IntegerField(blank=True, null=True)
    approved_date = models.DateTimeField()

class drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date = models.DateTimeField()
    received_date = models.DateTimeField()
    requested_by = models.IntegerField(blank=True, null=True) 
    pharmacy_id = models.IntegerField(blank=True, null=True)

class employees(models.Model):
    full_name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    work_unit = models.CharField(max_length = 200)
    job_position = models.CharField(max_length = 200)
    id_number = models.CharField(max_length = 200)
    gender_id = models.IntegerField(blank=True, null=True)

class employee_cards(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)
    card_id = models.IntegerField(blank=True, null=True)

class examination_catagory(models.Model):
    name = models.CharField(max_length = 200)

class examination_subcatagory(models.Model):
    name  = models.CharField(max_length = 200)
    examination_catagory_id = models.IntegerField(blank=True, null=True)

class examination_type(models.Model):
    name = models.CharField(max_length = 200)
    examination_subcatagory_id = models.IntegerField(blank=True, null=True)

class examination_type_options(models.Model):
    examination_type_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length = 200)

class floors(models.Model):
    name = models.CharField(max_length = 200)

class frequency(models.Model):
    name = models.CharField(max_length = 200)

class gender(models.Model):
    name = models.CharField(max_length = 200)

class issuances(models.Model):
    issued_date = models.DateField()
    drug_id = models.IntegerField(blank=True, null=True)
    pharmacy_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)

class item_type(models.Model):
    name = models.CharField(max_length = 200)

class laboratories(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    drug_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(max_length = 200)
    lab_technician_id = models.IntegerField(blank=True, null=True)

class lab_drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date = models.DateField()
    received_date = models.DateField()
    requested_by = models.IntegerField(blank=True, null=True) 
    laboratory_id = models.IntegerField(blank=True, null=True) 

class lab_examination(models.Model):
    priscription_id = models.IntegerField(blank=True, null=True)  
    lab_technicians_id = models.IntegerField(blank=True, null=True)  
    doctor_id = models.IntegerField(blank=True, null=True)  
    status = models.IntegerField(blank=True, null=True) 
    examination_type_id = models.IntegerField(blank=True, null=True)  
    request_date = models.DateField()
    result = models.CharField(max_length = 200) 
    result_date = models.DateField()
    remark = models.CharField(max_length = 200) 

class lab_technicians(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class meal_cheats(models.Model):
    time_cheated = models.DateTimeField()
    student_id = models.IntegerField(blank=True, null=True)
    meal_id = models.IntegerField(blank=True, null=True)

class meal_services(models.Model):
    time_served = models.DateTimeField()
    student_id = models.IntegerField(blank=True, null=True)
    meal_id = models.IntegerField(blank=True, null=True)

class meals(models.Model):
    meal_type_id = models.IntegerField(blank=True, null=True) 
    custom_start_time = models.TimeField()
    custom_end_time = models.TimeField()
    meal_date = models.DateField()
    cafeteria_id = models.IntegerField(blank=True, null=True)

class meal_types(models.Model):
    name = models.CharField(max_length = 200)
    default_start_time = models.TimeField()
    default_end_time = models.TimeField()
    
class menu(models.Model):
    name = models.CharField(max_length = 200) 
    controller = models.CharField(max_length = 200) 
    description = models.CharField(max_length = 200) 
    sequence = models.CharField(max_length = 200) 

class news(models.Model):
    name = models.CharField(max_length = 200) 
    posted_date = models.DateTimeField() 
    author = models.CharField(max_length = 200) 
    posted = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    content = models.TextField()

class nurses(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class opd(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    drug_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField()
    nurse_id = models.IntegerField(blank=True, null=True)

class opd_drug_requests(models.Model):
    requested_amount = models.IntegerField(blank=True, null=True)
    approved_amount = models.IntegerField(blank=True, null=True)
    requested_date= models.DateField() 
    received_date= models.DateField() 
    requested_by = models.IntegerField(blank=True, null=True)
    opd_id  = models.IntegerField(blank=True, null=True)

class parmacists(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class password_resets(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    identifier = models.CharField(max_length = 200)
    request_time = models.DateTimeField(auto_now_add=True)

class pending_id_prints(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

class permissions(models.Model):
    user_group_id = models.IntegerField(blank=True, null=True)
    submenu_id = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

class pharmacists(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class pharmacy(models.Model):
    drug_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    pharmacists_id = models.IntegerField(blank=True, null=True)

class placements(models.Model):
    year_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    dormitory_id = models.IntegerField(blank=True, null=True)
    check_in_date = models.DateTimeField(auto_now_add=True)
    check_out_date = models.DateTimeField(auto_now_add=True)
    cleared = models.IntegerField(blank=True, null=True)

class priscriptions(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    doctor_id = models.IntegerField(blank=True, null=True)
    examination_date = models.DateTimeField(auto_now_add=True)
    registration_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

class receptions(models.Model):
    employee_id = models.IntegerField(blank=True, null=True)

class refers(models.Model):
    refer_type_id = models.IntegerField(blank=True, null=True)
    priscription_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length = 200)

class refer_types(models.Model):
    name = models.CharField(max_length = 200)

class registration(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    student_id = models.IntegerField(blank=True, null=True)
    reception_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

class schools(models.Model):
    name = models.CharField(max_length = 200)

class settings(models.Model):
    propertys = models.CharField(max_length = 200)
    value = models.CharField(max_length = 200)

class sites(models.Model):
    name = models.CharField(max_length = 200)

class statuses(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

class students(models.Model):
    personal_name = models.CharField(max_length = 200)
    father_name = models.CharField(max_length = 200)
    grand_father_name = models.CharField(max_length = 200)
    id_number = models.CharField(max_length = 200)
    exam_registration_no = models.CharField(max_length = 200)
    barcode = models.CharField(max_length = 200)
    entry_batch_id = models.IntegerField(blank=True, null=True)
    current_batch_id = models.IntegerField(blank=True, null=True)
    admission_field_id  = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    gender_id = models.IntegerField(blank=True, null=True)
    disability_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    degree_id = models.IntegerField(blank=True, null=True)
    admission_type_id = models.IntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length = 200)
    manuplator_id = models.IntegerField(blank=True, null=True)
    archived = models.IntegerField(blank=True, null=True)

class student_cards(models.Model):
    date = models.DateField()
    card_id = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)

class submenu(models.Model):
    menu_id  = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length = 200)
    function = models.CharField(max_length = 200)
    description = models.TextField(max_length = 200)
    sequence = models.IntegerField(blank=True, null=True)

class temperature(models.Model):
    student_id = models.IntegerField(blank=True, null=True)
    temperature_station_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    temprature_range_id = models.IntegerField(blank=True, null=True)

class temperature_range(models.Model):
    valu = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)

class temperature_station(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

class tesme(models.Model):
    drug_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    pharmasist_id = models.IntegerField(blank=True, null=True)

class users(models.Model):
    user_group_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length = 200)
    active = models.IntegerField(blank=True, null=True)

class user_groups(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)

class user_station(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    temperature_station_id = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    status = models.IntegerField(blank=True, null=True)

class years(models.Model):
    name = models.IntegerField(blank=True, null=True)