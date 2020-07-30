from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile,User

city_choices = (
    ('Aswan','Aswan'),('Luxor','Luxor'),('Qena','Qena'),('Sohag','Sohag'),('Red Sea','Red Sea'),('Asyut','Asyut'),
    ('New Valley' , 'New Valley'),('Minya','Minya'),('Beni Suef' , 'Beni Suef'),
    ('Suez' , 'Suez'),('Cairo' , 'Cairo'),('Faiyum' , 'Faiyum'),('Ismailia' ,'Ismailia'),
    ('Sharqia' , 'Sharqia'),('Qalyubia' , 'Qalyubia'),('Monufia' , 'Monufia'),
    ('Gharbia' , 'Gharbia'),('North Sinai' , 'North Sinai'),('Port Said' , 'Port Said'),('Damietta' , 'Damietta'),
    ('Dakahlia' , 'Dakahlia'),('Kafr El Sheikh' , 'Kafr El Sheikh'),
    ('Beheira' , 'Beheira'),('Alexandria' , 'Alexandria'),('Matruh' , 'Matruh')
    )
blood_type_choices = (
        ('O−','O−'), ('O+','O+'),
        ('A-','A-'), ('A+','A+'),
        ('B-','B-'), ('B+','B+'),
        ('AB-','AB-'), ('AB+','AB+'))

BIRTH_YEAR_CHOICES = range(1920 ,2020,1)

class SignUpForm(UserCreationForm):
    FullName = forms.CharField(max_length=100)
    PhoneNumber = forms.CharField(max_length=11,)
    blood_type =forms.ChoiceField(choices=blood_type_choices)
    city = forms.ChoiceField(choices=city_choices)

    BIRTH_YEAR_CHOICES = range(1920 ,2020,1)
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2',)



     # this redefines the save function to include the fields you added
    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")

        user = super(SignUpForm, self).save(commit=True)
        user_profile = UserProfile(
        user=user,
        FullName = self.cleaned_data['FullName'],
        city = self.cleaned_data['city'],
        blood_type = self.cleaned_data['blood_type'],
        PhoneNumber= self.cleaned_data['PhoneNumber'],
       # profile_pic = self.cleaned_data['profile_pic'],
       birthday = self.cleaned_data['birthday'],
       



        )
        user_profile.save()
        return user,user_profile
