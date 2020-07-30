from django.urls import path
from .import views

app_name = 'bbank'

urlpatterns = [
    # bbank/
    path('about/', views.AboutView.as_view(), name='about'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('contact_us/',views.ContactUS.as_view(),name='contact_us'),
    path('blood_request/',views.PatientView.as_view(),name='patient'),     #patient Form


    # LOGIN
    #path('register/', views.register, name='register'),
   # path('login/',views.user_login,name='user_login'),
#path('user_logout/',views.user_logout,name='user_logout'),
  #  path('update/<pk>',views.UpdateUserInfo.as_view(),name='update'),
    #patient Form
]
