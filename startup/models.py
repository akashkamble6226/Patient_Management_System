from django.db import models

class All_Patients(models.Model):

    fname = models.CharField(max_length=255, unique=True) 
    date = models.DateField()
    mo_no = models.CharField(max_length=10) 
    age = models.CharField(max_length=3)
   
    CATEGORY_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    



    
    final_digno = models.CharField(max_length=255,null=True,blank=True)  
    blood_press= models.CharField(max_length=255,null=True,blank=True)
     

    cheapcomp = models.CharField(max_length=255)  
    allergy = models.CharField(max_length=255)  
    provisdigno = models.CharField(max_length=255)  
    treatment = models.CharField(max_length=255)  
    clinicalnotes = models.CharField(max_length=255)



    class Meta:
        get_latest_by = ['id'] 
    
class Old_Patients(models.Model):
    fname = models.CharField(max_length=255, unique=False)  
    date = models.DateField()
    age = models.CharField(max_length=3)

    total_fee = models.IntegerField()
    given_fee = models.IntegerField()
    remaining_fee = models.IntegerField()   

    
    cheapcomp = models.CharField(max_length=255)  
    allergy = models.CharField(max_length=255)  
    provisdigno = models.CharField(max_length=255)  
    treatment = models.CharField(max_length=255)  
    clinicalnotes = models.CharField(max_length=255)

    final_digno = models.CharField(max_length=255,null=True,blank=True)  
    blood_press= models.CharField(max_length=255,null=True,blank=True)


    temporary_add = models.CharField(max_length=250)
    parmanent_add = models.CharField(max_length=250)

    parmanent_disease = models.CharField(max_length=250)

    ipd = models.CharField(max_length=250)

    class Meta:
        get_latest_by = ['fname']  



