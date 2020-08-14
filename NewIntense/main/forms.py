from django import forms
from .models import Contact,Apply ,Enquiry,ApplyP
from phonenumber_field.formfields import PhoneNumberField
from django.forms.utils import ValidationError
from django.core.validators import RegexValidator
from django.core import validators

GND_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

class ContactForm(forms.ModelForm):
    name=forms.CharField(required =True,validators=[RegexValidator(r'[a-zA-Z]+', 'Only  characters.')])
    mail=forms.EmailField(required =True)
    contact_Number=PhoneNumberField()
    message=forms.CharField(widget=forms.Textarea(
                                        attrs={
                                            'rows' : 4, 
                                            'cols' : 23,
                                            'class' : 'form-control'
                                            }))

    class Meta:
        model = Contact
        fields = [
            'name',
            'mail',
            'contact_Number',
            'message']
        

class ApplicationForm(forms.ModelForm):
    name=forms.CharField(required =True,validators=[RegexValidator(r'[a-zA-Z]+', 'Only  characters.')])
    contact_Number=PhoneNumberField()
    email=forms.EmailField(required =True)
    current_City=forms.CharField(required =True)
    class Meta:
        model = Apply
        fields = [
            'name',
            'email',
            'contact_Number',
            'gender',
            'current_City',
            'upload_Resume']
    
        
class ApplicationFormP(forms.ModelForm):
    name=forms.CharField(required =True,validators=[RegexValidator(r'[a-zA-Z]+', 'Only  characters.')])
    contact_Number=PhoneNumberField()
    gender = forms.CharField(label='Gender',widget=forms.Select(choices=GND_CHOICES))
    email=forms.EmailField(required =True)
    current_City=forms.CharField(required =True)
    class Meta:
        model = ApplyP
        fields = [
            'name',
            'email',
            'contact_Number',
            'gender',
            'current_City',
            'upload_Resume']
        

class EnquiryForm(forms.ModelForm):
    name=forms.CharField(required =True,validators=[RegexValidator(r'[a-zA-Z]+', 'Only  characters.')])
    company=forms.CharField(required =True)
    post=forms.CharField(required =True)
    mail=forms.EmailField(required =True)
    contact_Number=PhoneNumberField()
    city=forms.CharField(required =True)
    description=forms.CharField(widget=forms.Textarea(
                                        attrs={
                                            'rows' : 4, 
                                            'cols' : 23,
                                            'class' : 'form-control'
                                            }))
    class Meta :
        model = Enquiry
        fields = [
            'name',
            'company',
            'post',
            'mail',
            'contact_Number',
            'city',
            'description'
        ]
       
   
