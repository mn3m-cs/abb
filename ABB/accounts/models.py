from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profiles')
    # TODO pics not deleted when user is deleted 
    #additional
    PhoneNumber = models.CharField('Phone Number',max_length=11,)
    FullName = models.CharField('Full Name',max_length=100)
    city_choices = (
    ('Aswan','Aswan'),('Luxor','Luxor'),('Qena','Qena'),('Sohag','Sohag'),('Red Sea','Red Sea'),('Asyut','Asyut'),
    ('New Valley' , 'New Valley'),('Minya','Minya'),('Beni Suef' , 'Beni Suef'),
    ('Suez' , 'Suez'),('Cairo' , 'Cairo'),('Faiyum' , 'Faiyum'),('Ismailia' ,'Ismailia'),
    ('Sharqia' , 'Sharqia'),('Qalyubia' , 'Qalyubia'),('Monufia' , 'Monufia'),
    ('Gharbia' , 'Gharbia'),('North Sinai' , 'North Sinai'),('Port Said' , 'Port Said'),('Damietta' , 'Damietta'),
    ('Dakahlia' , 'Dakahlia'),('Kafr El Sheikh' , 'Kafr El Sheikh'),
    ('Beheira' , 'Beheira'),('Alexandria' , 'Alexandria'),('Matruh' , 'Matruh')

 
    )
    city = models.CharField(max_length=264,choices = city_choices)

    profile_pic = models.ImageField('Profile Picture',upload_to='profile_pics',blank=True,help_text="Upload your pic")
    
    blood_type_choices = (
        ('O−','O−'), ('O+','O+'),
        ('A-','A-'), ('A+','A+'),
        ('B-','B-'), ('B+','B+'),
        ('AB-','AB-'), ('AB+','AB+'),
    )
    blood_type = models.CharField(max_length=3,choices=blood_type_choices,)

    birthday = models.CharField(max_length=8)


    def __str__(self):
        return self.user.username

