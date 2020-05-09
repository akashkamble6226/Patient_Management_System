from django import forms
from startup.models import All_Patients


class All_Patients_Form(forms.ModelForm):

    your_name = forms.CharField(label='Your name', max_length=100)
    
    class Meta:
        model = All_Patients
        fields = "__all__"




