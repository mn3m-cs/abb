from django.contrib import admin
from .models import UserProfile



class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ('user','blood_type','city')
    list_filter = ['city','blood_type',]
    #search_fields = ['FullName',]

admin.site.register(UserProfile,UserProfileModelAdmin)
