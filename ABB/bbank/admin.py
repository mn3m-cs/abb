from django.contrib import admin
from .models import ContactUS,Patient
from .forms import PatientForm,ContactUSForm
 

class PatientModelAdmin(admin.ModelAdmin):
    readonly_fields = ('request_time',)
    form = PatientForm
admin.site.register(Patient,PatientModelAdmin)


class ContactUSModelAdmin(admin.ModelAdmin):
    readonly_fields = ('sending_time',)
    form = ContactUSForm
admin.site.register(ContactUS,ContactUSModelAdmin)