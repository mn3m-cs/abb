from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views  as auth_views
from django.conf.urls import url

app_name= 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    #my account
    path('settings/account/',views.UserUpdateView.as_view(),name='my_account'),
    path('settings/profile/',views.ProfileUpdateView.as_view(),name='profile'),
    
]