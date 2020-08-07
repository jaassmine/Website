from django.shortcuts import render, redirect
from .models import Job , Apply
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ContactForm,ApplicationForm ,EnquiryForm,ApplicationFormP
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.views import APIView 



def homepage(request):
	# if request.user.is_authenticated:
	# 	if request.user.is_partner:
	# 		return redirect('homepage')
	# 	else:
	# 	    return redirect('homepage')
	# else:
		return render(request = request,
					template_name = "home.html",
					# context = {"jobs" : Job.objects.all}
					)

def about(request):
	return render(request = request,
		 		  template_name = "about.html",
				  # context = {"jobs" : Job.objects.all}
				  )

def faq(request):
	return render(request= request,
			template_name = "faq.html",
	)
def employer(request):
	if request.method=='POST':
		form = EnquiryForm(request.POST)
		if form.is_valid():
			form.save()

	form = EnquiryForm()
	return render(request,'employer.html',{'form':form} )
	# return render(request = request,
	# 			  template_name = "employer.html",
	# 			  # context = {"jobs" : Job.objects.all}
	# 			  )

def contact(request):
	if request.method=='POST':
		message_name = request.POST['name']
		message_email = request.POST['mail']
		# message_contact = request.POST['contact']
		message = request.POST['message']

		send_mail(
			'Message from '+message_name, #subject
			message ,  #message
			message_email ,  # from emails
			['intense@gmail.com'],
		)
		messages.info(request , message_name)
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()

	form = ContactForm()
	return render(request,'contact.html',{'form':form} )
	# return render(request = request,
	# 			  template_name = "contact.html",
	# 			  # context = {"jobs" : Job.objects.all}
	# 			  )
	
@login_required(login_url= 'account:login')
def jobs(request):
	jobArr= Job.objects.all()
	role_val = request.GET.get('role')
	city_val = request.GET.get('city')
	district_val = request.GET.get('role')
	if role_val !='' and role_val is not None :
		jobArr = jobArr.filter(job_title__icontains = role_val)
	elif city_val !='' and city_val is not None :
		jobArr = jobArr.filter(job_loc__icontains = city_val) 
	if not jobArr :
		messages.error(request,'Currently there are 0 jobs')
	context = {
		'jobArr' : jobArr
	}
	return render(request= request, 
				  template_name = "jobs.html",
				  context = context)

@login_required(login_url='account:login')
def apply(request,pk):
	jjob = Job.objects.get(pk=pk)
	cc=Candidate.objects.get(user =  request.user)
	# initial_data={
	# 	'candidate': request.user.username,
	# 	'job' : jjob.job_title
	# }
	if Apply.objects.filter(job = jjob, candidate = cc).exists():
		messages.error(request,'You have already applied for this job')
	else :
		if request.method == 'POST':
			form = ApplicationForm( request.POST , request.FILES )
			if form.is_valid():
				post = form.save(commit = False)
				#post.candidate = request.user.username
				post.candidate = Candidate.objects.get(user =  request.user)
				post.job = Job.objects.get(pk = pk )
				post.save()
				messages.success(request,' You have applied  successfully for this job')
				# form.save()
			else:
				print("wRONG Data")

	form = ApplicationForm()
	return render(request,'apply.html',{'form':form} )
	# return render(request = request,
	# 			  template_name = "apply.html",
	# 			  # context = {"jobs" : Job.objects.all}
	# 			  )

@login_required(login_url='account:loginp')
def applyp(request,pk):
	# initial_data={
	# 	'candidate': request.user.username,
	# 	'job' : jjob.job_title
	# }
	if request.method == 'POST':
		form = ApplicationFormP( request.POST , request.FILES )
		if form.is_valid():
			post = form.save(commit = False)
			#post.candidate = request.user.username
			post.partner = Partner.objects.get(user =  request.user)
			post.job = Commission.objects.get(pk = pk )
			post.save()
			messages.success(request,' You have applied  successfully for this job')
			# form.save()
		else:
			print("wRONG Data")

	form = ApplicationFormP()
	return render(request,'applp.html',{'form':form} )

@login_required(login_url='account:loginp')
def patcomm(request):
	jobAr= Commission.objects.all()
	role_val = request.GET.get('role')
	city_val = request.GET.get('city')
	district_val = request.GET.get('role')
	if role_val !='' and role_val is not None:
		jobAr = jobAr.filter(job_title__icontains = role_val) 
	elif city_val !='' and city_val is not None:
		jobAr = jobAr.filter(job_loc__icontains = city_val) 
	if not jobAr :
		messages.error(request,'Currently there are 0 jobs')
	context = {
		'jobAr' : jobAr
	}

	return render(request = request,
				  template_name = "pat_com.html",
				  context = context
				  )


class JobViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = JobSerializer
	queryset = serializer_class.Meta.model.objects.all()


class ApplyJobApiView(CreateAPIView):
	serializer_class = ApplicantSerializer
	http_method_names = [u'post']
	permission_classes = [IsAuthenticated]

	def create(self , request , *args , **kwargs):
		serializer = self.get_serializer(data = request.data)
		serializer.is_valid(raise_exception = True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data , status = status.HTTP_201_CREATED , headers = headers)

class ApplyAPIView(APIView):
	
	def get(self , request):
		apply = Apply.objects.all()
		serializer = ApplicantSerializer(employer , many = True)
		return Response(serializer.data)
