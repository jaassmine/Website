from django.contrib import admin
from .models import Job
from .models import Contact,Apply,Enquiry,Commission,ApplyP

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name' , 'mail' , 'contact_Number')


class JobAdmin(admin.ModelAdmin):
	fields = [
				"job_title",
				"job_des",
				"job_company",
				"job_sal", 
				"job_loc",
				"city",
				"gender",
				"timing",
				"qualification"
				]
	list_display = ('job_title' , 'job_company' ,'job_sal' , 'job_loc' ,'city')
	list_filter = ('job_company' , 'job_title','job_loc','city')

class CommissionAdmin(admin.ModelAdmin):
	fields = [
				"job_title",
				"company_title",
				"job_des",
				"job_sal", 
				"job_loc",
				"city",
				"job_exp",
				"age",
				"gender",
				"pat_com",
				"time",
				"g_period"
				]
	list_display = ('job_title' , 'company_title' ,'job_sal' , 'job_loc' )
	list_filter = ('company_title' , 'job_title','job_loc','city')	

class ApplyAdmin(admin.ModelAdmin):

	list_display = ('candidate' , 'job', 'name' ,'email','contact_Number')
	list_filter = ('candidate' , 'job','current_City','gender')	
	search_fields = ['job__job_title' , 'candidate__user__username']

class EnquiryAdmin(admin.ModelAdmin):

	list_display = ('company' , 'post' , 'mail' , 'contact_Number')
	list_filter = ('post' , 'company')

class ApplyPAdmin(admin.ModelAdmin):

	list_display = ('partner' , 'job', 'name' ,'email',,'contact_Number')
	list_filter = ('partner' , 'job','current_City','gender')	
	search_fields = ['job__job_title' , 'partner__user__username']

admin.site.register(Job , JobAdmin)
admin.site.register(Contact , ContactAdmin)
admin.site.register(Apply , ApplyAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Commission , CommissionAdmin)
admin.site.register(ApplyP,ApplyPAdmin)
