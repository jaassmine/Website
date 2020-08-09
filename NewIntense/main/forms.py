from django import forms
from .models import Contact,Apply ,Enquiry,ApplyP


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','mail','contact_Number','message')
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control' }),
            'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'message':forms.Textarea(attrs={'rows' : 4, 'cols' : 23 , 'class' : 'form-control'})
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('name','email','contact_Number','gender','current_City','upload_Resume')
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'current_City':forms.TextInput(attrs={'class' : 'form-control'}),
            # 'upload_Resume' :forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }
        
class ApplicationFormP(forms.ModelForm):
    class Meta:
        model = ApplyP
        fields = ('name','email','contact_Number','gender','current_City','upload_Resume')
        widgets={
            # 'candidate': forms.TextInput(attrs={'class': 'form-control'}),
            # 'job': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
            'current_City':forms.TextInput(attrs={'class' : 'form-control'}),
            # 'upload_Resume' :forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }

class EnquiryForm(forms.ModelForm):
    class Meta :
        model = Enquiry
        fields = ('name','company','post','mail','contact_Number','city','description')
        widgets={
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'company' : forms.TextInput(attrs={'class': 'form-control'}),
                'post': forms.TextInput(attrs={'class': 'form-control'}),
                'mail': forms.EmailInput(attrs={'class': 'form-control' }),
                'contact_Number': forms.TextInput(attrs={'class': 'form-control'}),
                'city':forms.TextInput(attrs={'class' : 'form-control'}),
                'description':forms.Textarea(attrs={'rows' : 4, 'cols' : 23,'class' : 'form-control'})
                }
