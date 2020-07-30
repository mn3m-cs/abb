from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,UpdateView,DeleteView,DetailView,FormView)
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import User,ContactUS
from .forms import ContactUSForm,PatientForm
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.utils.html import format_html
from accounts.models import UserProfile

class AboutView(TemplateView):
    template_name = "bbank/about.html"


class HomeView(TemplateView):
    template_name = 'bbank/home.html'

# LOGIN_views
'''
@user_passes_test(lambda u: u.is_anonymous) # this will print error if the user try going to register page while is login TODO we should handle this with better way
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user = user #user is the foregin key 
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered = True
            #return HttpResponseRedirect(reverse('bbank:home')) 
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'bbank/register.html', {'user_form': user_form,
                                                   'registered': registered,
                                                   'profile_form':profile_form})
                                                   
@user_passes_test(lambda u: u.is_anonymous) # this will print error if the user try going to register page while is login
def user_login(request):
    inv=False
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('bbank:home'))
            else:
                return HttpResponse("YOUR ACCOUNT IS NOT ACTIVE")
        else:
            #TODO: rerturn form errors 'invalid'
            return HttpResponse("invalid Credentials")
    else:
        return render(request,'bbank/login.html',{'inv':inv})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bbank:home'))

def contact_us(request):
    #contacted = False
    if request.method == 'POST':
        contact_form = ContactUSForm(data=request.POST)
        if contact_form.is_valid():
            #contacted = True
            contact_form.save()
            # here we should construct msg body 
            send_mail("ContactUS","please help",'mohamedabdo581@gmail.com',('mohamed.ms6@aun.edu.eg',))
            return HttpResponseRedirect(reverse('bbank:home'))
        
        else:
            print(contact_form.errors())
        
    else:
        contact_form = ContactUSForm()

    return render (request,'bbank/contact_us.html',{'contact_form':contact_form})
'''

class PatientView(LoginRequiredMixin,SuccessMessageMixin,FormView):
    template_name = 'bbank/patient_form.html'
    form_class = PatientForm
    success_url = '/bbank/home/'


    def get_success_message(self, cleaned_data):
        # RETURN NUMBER OF DONORS RECIEVED REQUEST IN SUCCESS MESSAGE
        pcity = cleaned_data['city']
        pblood =cleaned_data['patient_blood_type']
        available_donors = UserProfile.objects.filter(city=pcity,blood_type=pblood)
        number_of_available_donors =  len(available_donors)
        print(number_of_available_donors) 

        if number_of_available_donors > 0 : #<!-- TODO from jose course see how to use pluralize
            suc_msg = format_html(" <strong> {} </strong> donors with blood type<strong> {} </strong> from <strong> {} </strong> recieved your request successfully, we wish a fast recovery ",
            number_of_available_donors,pblood,pcity)
            # send email with suc_msg
        else:
            suc_msg =format_html("We are sorry, No available donors from <strong> {} </strong> with blood type <strong> {} </strong>",
            pcity,pblood)

        return suc_msg

    def form_valid(self, form):
        form.save()
        form.search() # function that find donors and send emails
        return super().form_valid(form)

class ContactUS(SuccessMessageMixin,FormView):
    template_name = 'bbank/contact_us.html'
    form_class = ContactUSForm
    success_url = '/bbank/home/'

    def get_success_message(self, cleaned_data):
        return 'Thanks, Your email has been sent successfully'
    
    def form_valid(self, form):
        form.save()
        form.send()
        return super().form_valid(form)

