from django.urls import path
from . import views
from .views import *


app_name = "main"
urlpatterns = [
	path('',views.homepage , name = "homepage"),
	path('about/' ,views.about , name = "about"),
	path('employer/', views.employer, name = "employer"),
    path('contact/', views.contact, name = "contact"),
	# path('partner/', views.partner, name = "partner"),
    # path('log_sign/',views.log_sign , name= "log_sign"), 
    # path('register/', views.register ,  name = "register"),
    # path("candidate.html", views.candidate, name='candidate'), 
    path("jobs/", views.jobs, name='jobs'), 
    path("patcomm/", views.patcomm, name='patcomm'),
    # path("apply/", ApplyView.as_view(), name='apply'), 
    # path("patcomm.html", views.apply, name='patcomm'), 
    path('apply/<int:pk>/', views.apply, name = 'apply'),
    path('applyp/<int:pk>/', views.applyp, name = 'applyp'),
    path('faq/' , views.faq , name = 'faq'),
]

