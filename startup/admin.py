from django.contrib import admin


from .models import All_Patients,Old_Patients

# Register your models here.
admin.site.register(All_Patients)
admin.site.register(Old_Patients)