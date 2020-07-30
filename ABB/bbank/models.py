from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ContactUS(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    email = models.EmailField()
    sending_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

class Patient(models.Model):
        
    patient_name = models.CharField(max_length=50)
    patient_blood_type_choices = (
        ('O−','O−'), ('O+','O+'),
        ('A-','A-'), ('A+','A+'),
        ('B-','B-'), ('B+','B+'),
        ('AB-','AB-'), ('AB+','AB+'))

    city_choices = (
    ('Aswan','Aswan'),('Luxor','Luxor'),('Qena','Qena'),('Sohag','Sohag'),('Red Sea','Red Sea'),('Asyut','Asyut'),
    ('New Valley' , 'New Valley'),('Minya','Minya'),('Beni Suef' , 'Beni Suef'),
    ('Suez' , 'Suez'),('Cairo' , 'Cairo'),('Faiyum' , 'Faiyum'),('Ismailia' ,'Ismailia'),
    ('Sharqia' , 'Sharqia'),('Qalyubia' , 'Qalyubia'),('Monufia' , 'Monufia'),
    ('Gharbia' , 'Gharbia'),('North Sinai' , 'North Sinai'),('Port Said' , 'Port Said'),('Damietta' , 'Damietta'),
    ('Dakahlia' , 'Dakahlia'),('Kafr El Sheikh' , 'Kafr El Sheikh'),
    ('Beheira' , 'Beheira'),('Alexandria' , 'Alexandria'),('Matruh' , 'Matruh'))
    
    patient_blood_type = models.CharField(max_length=3,choices=patient_blood_type_choices,)

    city = models.CharField(max_length=264,choices = city_choices)
    PhoneNumber = models.CharField('Phone Number',max_length=11)
    hospital = models.CharField(max_length=264,)
    additional_info = models.CharField(max_length=1000,blank=True,null=True)
    request_time = models.DateTimeField(auto_now_add=True) # handled in the admin
    

    def __str__(self):
        return self.patient_name
         