from django.db import models
from account.models import Candidate
from phonenumber_field.modelfields import PhoneNumberField
from account.models import User , Candidate,Partner

# Create your models here.
GND_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
class Job(models.Model):
	candidates = models.ForeignKey(Candidate , null = True , on_delete= models.SET_NULL)
	job_title =  models.CharField(max_length = 50)
	job_company = models.CharField(max_length = 100 , null = True)
	job_des = models.TextField()
	job_sal = models.IntegerField()
	job_loc = models.CharField(max_length = 500)
	gender=models.CharField(max_length = 100)
	timing=models.CharField(max_length = 500)
	qualification=models.CharField(max_length = 500)
	city = models.CharField(max_length = 50)
	def __str__(self):
		return self.job_title

class Contact(models.Model):
	name=models.CharField(max_length=100)
	mail=models.EmailField()
	contact_Number=PhoneNumberField()
	message=models.TextField()

	def __str__(self):
		return self.name


class Apply(models.Model):
	candidate = models.ForeignKey(Candidate, null= True , on_delete= models.SET_NULL)
	job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
	name=models.CharField(max_length=100)
	contact_Number=PhoneNumberField()
	gender = models.CharField(choices=GND_CHOICES, max_length=128,null=True)
	email=models.EmailField()
	current_City=models.CharField(max_length=200)
	upload_Resume=models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	
		# return f'{self.candidate.username()}Applied'

class Enquiry(models.Model):
	name=models.CharField(max_length=100)
	company=models.CharField(max_length=100)
	post=models.CharField(max_length=100)
	mail=models.EmailField()
	contact_Number=PhoneNumberField()
	city=models.CharField(max_length=100)
	description=models.TextField()

	def __str__(self):
		return self.company

class Commission(models.Model):
	partners = models.ForeignKey(Partner , null = True , on_delete= models.SET_NULL)
	job_title =  models.CharField(max_length = 100)
	company_title =  models.CharField(max_length = 100)
	job_loc = models.CharField(max_length = 500)
	city = models.CharField(max_length = 50)
	job_sal = models.CharField(max_length = 500)
	job_exp=models.CharField(max_length = 100)
	job_des = models.TextField()
	age=models.CharField(max_length = 500)
	gender=models.CharField(max_length = 100)
	pat_com=models.CharField(max_length = 100)
	time=models.CharField(max_length = 500)
	g_period=models.CharField(max_length = 500)

	def __str__(self):
		return self.job_title

class ApplyP(models.Model):
	partner = models.ForeignKey(Partner, null= True , on_delete= models.SET_NULL)
	job = models.ForeignKey(Commission, null=True, on_delete=models.SET_NULL)
	name=models.CharField(max_length=100)
	contact_Number=PhoneNumberField()
	gender = models.CharField(choices=GND_CHOICES, max_length=128,null=True)
	email=models.EmailField()
	current_City=models.CharField(max_length=200)
	upload_Resume=models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
