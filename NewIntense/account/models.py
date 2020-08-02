# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

ORG_CHOICES = (
   ('PA', 'Placement Agency'),
   ('FR', 'Freelancer'),
   ('N','NGO'),
   ('TI','Training Institute'),
   ('CC','Cyber Cafe'),
   ('CLG','College'),
)

class User(AbstractUser):
    is_candidate = models.BooleanField(default = False)
    is_partner = models.BooleanField(default = False)
    

class Candidate(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE , primary_key = True)
    # first_name=models.CharField(max_length=20)
    # last_name=models.CharField(max_length=20)
    # email=models.EmailField()
    phone_no = models.CharField(max_length = 10)
    father_name=models.CharField(max_length=50)
    education=models.CharField(max_length=100)
    PAN_number=models.CharField(max_length=10)
    Aadhar_number=models.CharField(max_length=13)
    location = models.CharField(max_length = 20)
    last_salary = models.CharField(max_length = 50 ,default="Not Applicable")
    last_company= models.CharField(max_length = 50,default='Not Applicable')
    
    def __str__(self):
        return self.user.username
    
class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    # first_name=models.CharField(max_length=20)
    # last_name=models.CharField(max_length=20)
    # email=models.EmailField()
    organisation_type = models.CharField(choices=ORG_CHOICES, max_length=128,null=True)
    organisation_name = models.CharField(max_length = 20)
    organisation_location = models.CharField(max_length = 20)
    phone_no = models.CharField(max_length = 10)
    experience = models.CharField(max_length = 10)
    def __str__(self):
        return self.user.username