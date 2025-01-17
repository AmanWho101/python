# Generated by Django 5.1.5 on 2025-01-15 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission_fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Admission_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('accronym', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('location_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('accronym', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Disabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('diseases_code', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dosage_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Examination_catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_technicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Refer_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertys', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unit_price', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('batch_number', models.CharField(max_length=200)),
                ('expire_date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.category')),
            ],
        ),
        migrations.CreateModel(
            name='Drug_infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('received_date', models.DateField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.card')),
            ],
        ),
        migrations.CreateModel(
            name='Examination_subcatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('examination_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.examination_catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Examination_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('examination_subcatagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.examination_subcatagory')),
            ],
        ),
        migrations.CreateModel(
            name='Examination_type_options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('examination_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.examination_type')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('remark', models.TextField(max_length=200)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
                ('lab_technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.lab_technicians')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_drug_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_amount', models.IntegerField(blank=True, null=True)),
                ('approved_amount', models.IntegerField(blank=True, null=True)),
                ('requested_date', models.DateField()),
                ('received_date', models.DateField()),
                ('requested_by', models.IntegerField(blank=True, null=True)),
                ('laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.laboratories')),
            ],
        ),
        migrations.CreateModel(
            name='OPD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('remark', models.TextField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.nurses')),
            ],
        ),
        migrations.CreateModel(
            name='OPD_drug_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_amount', models.IntegerField(blank=True, null=True)),
                ('approved_amount', models.IntegerField(blank=True, null=True)),
                ('requested_date', models.DateField()),
                ('received_date', models.DateField()),
                ('requested_by', models.IntegerField(blank=True, null=True)),
                ('opd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.opd')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
                ('pharmacists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.pharmacists')),
            ],
        ),
        migrations.CreateModel(
            name='Drug_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_amount', models.IntegerField(blank=True, null=True)),
                ('approved_amount', models.IntegerField(blank=True, null=True)),
                ('requested_date', models.DateTimeField()),
                ('received_date', models.DateTimeField()),
                ('requested_by', models.IntegerField(blank=True, null=True)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Priscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examination_date', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, null=True)),
                ('request_date', models.DateField()),
                ('result', models.CharField(max_length=200)),
                ('result_date', models.DateField()),
                ('remark', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.doctors')),
                ('examination_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.examination_type')),
                ('lab_technicians', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.lab_technicians')),
                ('priscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.priscriptions')),
            ],
        ),
        migrations.CreateModel(
            name='Drug_prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('dosage', models.CharField(max_length=200)),
                ('student_signature', models.CharField(max_length=200)),
                ('delivery_date', models.DateTimeField()),
                ('remark', models.CharField(max_length=200)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.diseases')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
                ('pharmasist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.pharmacists')),
                ('priscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.priscriptions')),
            ],
        ),
        migrations.CreateModel(
            name='Refers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(max_length=200)),
                ('priscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.priscriptions')),
                ('refer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.refer_types')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('reception', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.reception')),
            ],
        ),
        migrations.AddField(
            model_name='priscriptions',
            name='registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.registration'),
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.schools')),
            ],
        ),
        migrations.CreateModel(
            name='Active_statuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.IntegerField(blank=True, null=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.statuses')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('grand_father_name', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=200)),
                ('exam_registration_no', models.CharField(max_length=200)),
                ('barcode', models.CharField(max_length=200)),
                ('entry_batch', models.IntegerField(blank=True, null=True)),
                ('current_batch', models.IntegerField(blank=True, null=True)),
                ('ip_address', models.CharField(max_length=200)),
                ('manuplator_id', models.IntegerField(blank=True, null=True)),
                ('archived', models.IntegerField(blank=True, null=True)),
                ('admission_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.admission_fields')),
                ('admission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.admission_types')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.degrees')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.departments')),
                ('disability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.disabilities')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.gender')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.statuses')),
            ],
        ),
        migrations.CreateModel(
            name='Student_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.card')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.students')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.students'),
        ),
        migrations.AddField(
            model_name='priscriptions',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.students'),
        ),
        migrations.CreateModel(
            name='Pending_id_prints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.students')),
            ],
        ),
        migrations.CreateModel(
            name='Tesme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.drugs')),
                ('pharmasist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssms_model.pharmacists')),
            ],
        ),
    ]
