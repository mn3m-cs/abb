from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login 
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import UpdateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.utils.html import format_html
from django.contrib.auth.decorators import user_passes_test

def signup(request):
    if request.user.is_authenticated:
       return HttpResponseRedirect('../login')

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
          #  login(request,user) # when edit save method of form , can't use this here
            messages.success(request,format_html(
                     '''Your account has been created successfully , 
                      <a class="alert-link" href='../../login/'> Login here </a> '''))
            return redirect('bbank:home')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = ('first_name','last_name','email')
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user



class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfile
    fields = ('FullName','PhoneNumber','city','blood_type')
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user.profiles # profiles is the related name
    