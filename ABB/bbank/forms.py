from django import forms
from .models import ContactUS,Patient
from accounts.models import UserProfile
from django.core import validators
from django.core.mail import send_mail
from django.contrib.auth.models import User



class ContactUSForm(forms.ModelForm):
    Twitter = forms.URLField(initial='http://') # <!-- TODO instead of twitter , socail contact method : and choose whats or fb or twitter
    class Meta:
        model = ContactUS
        fields = ('subject','message','email')

        widgets = {
            'message':forms.Textarea(),
            
        }
    BIRTH_YEAR_CHOICES = range(1920 ,2020,1)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        subject = all_cleaned_data['subject']
        message = all_cleaned_data['message']
        return all_cleaned_data
    
    def send(self):
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        send_mail(subject,message,'mohamedabdo581@gmail.com',('mohamed.ms6@aun.edu.eg',))
        # <!--TODO curenntly, the sender will be always my email , because of mail server -->

class PatientForm(forms.ModelForm):
 
    class Meta:
        model = Patient
        fields =('patient_name','PhoneNumber','hospital','patient_blood_type','city','additional_info',)

        widgets = {
            'hospital':forms.TextInput(attrs={'placeholder':'place where the patient is, OR place donor should go'}),
            'additional_info':forms.Textarea(),
        }

    def clean(self):
        all_clean_data=super().clean()
        pname = all_clean_data['patient_name']
        pblood = all_clean_data['patient_blood_type']
        pcity = all_clean_data['city']
        return all_clean_data

    def search(self):
        pcity = self.cleaned_data['city']
        pblood = self.cleaned_data['patient_blood_type']
        pname = self.cleaned_data['patient_name']
        pphonenumber = self.cleaned_data['PhoneNumber']
        phospital =self.cleaned_data['hospital']
        padditionalinfo = self.cleaned_data['additional_info']
        print('ptient city is ' ,pcity)

        available_donors = UserProfile.objects.filter(city=pcity,blood_type=pblood)
        number_of_available_donors =  len(available_donors)
        print(number_of_available_donors) #TODO reuturn number of donors in 
        donors = list(available_donors)
         
        # get list with available donors emails 
        dd = []
        for donor in donors:
            user = User.objects.get(username=donor)
            dd.append(user.email)
        print(dd)

        #Send mails
        msg = ''' Hi, There is patient life you can save it ,
        * Patinet Informations * 
        Patient Name: {} 
        Patient Blood Type : {}  
        Patient Location : {}
        ---------------- 
        * Communicatio info *
        Phone Number : {} 
        Hospital : {}
        Additional info : {}

        '''.format(pname,pblood,pcity,pphonenumber,phospital,padditionalinfo)
        send_mail('blood request',msg,'mohamedabdo581@gmail.com',dd) #mohamed.ms6@aun.edu.eg
        # TODO: add patient forms to excel sheet ( date, name , blood , and emails of the donors have been emailed)
        return number_of_available_donors
        