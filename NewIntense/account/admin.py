from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Candidate, User, Partner
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name' , 'last_name' , 'email' ,'is_candidate' , 'is_partner')
    list_filter = ('username' , 'is_candidate' , 'is_partner')



# class CandidateAdmin(admin.ModelAdmin):
#     list_display = ( 'phone_no', 'fath' )
#     # list_filter = ()

class PartnerAdmin(admin.ModelAdmin):

    list_display = ('organisation_name' , 'organisation_type', 'organisation_location', 'phone_no')
    list_filter = ('organisation_name' , 'organisation_type')

admin.site.register(User , UserAdmin)
admin.site.register(Candidate)
admin.site.register(Partner , PartnerAdmin)
