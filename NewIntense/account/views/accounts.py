from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required 
from ..decorators import unauthenticated_user
from ..models import Candidate,Partner
from main.models import Apply , Job, Commission,ApplyP
from django.core.paginator import Page,Paginator,PageNotAnInteger,EmptyPage

# def home(request):
#     # if request.user.is_authenticated:
#     #     if request.user.is_partner:
#     #         return redirect('homePar')
#     #     else:
#     #         return redirect('homeCan')
#     # else:
#         return render(request, 'home.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username , password = password)
        if user is not None and user.is_candidate == True :
            login(request , user)
            return redirect('account:candidate_dash')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request , 'login.html')
    return render(request = request,
            template_name = 'login.html' 
        )

def loginpageP(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username , password = password)
        if user is not None and user.is_partner == True:
            login(request , user)
            return redirect('account:partner_dash')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request , 'loginp.html')
    return render(request = request,
            template_name = 'loginp.html' 
        )
def logoutuser(request):
    logout(request)
    return redirect('main:homepage')

@login_required(login_url = 'account:login')
def candidate_dash(request):
   
    return render(request = request , template_name = 'candidateDash.html')


@login_required(login_url = 'account:login')
def candapply(request):
    # candidate = Candidate.objects.get(user_id = pk)
    candidateJ = Candidate.objects.get(user =  request.user)
    applicant = Apply.objects.filter(candidate = candidateJ)
    # jobs = Apply.objects.filter(candidate =request.user.id)
    job_id = applicant.values("job")
    jobs = Job.objects.filter(id__in = job_id).values() 
    page = request.GET.get('page', 1)
	paginator = Paginator(jobs, 18)
	try:
		jjob = paginator.page(page)
	except PageNotAnInteger:
		jjob = paginator.page(1)
	except EmptyPage:
		jjob = paginator.page(paginator.num_pages)
    if not jobs :
        messages.error(request,'You have 0 Applications')
    context = { 'jobs' :jobs ,
                'jjob' :jjob
              }
    return render(request = request , template_name = 'cand_apply.html' , context = context)


@login_required(login_url = 'account:loginp')
def partner_dash(request):

    return render(request = request , template_name = 'partnerDash.html')


@login_required(login_url = 'account:loginp')
def patapply(request):
    try :
        partnerJ = Partner.objects.get(user =  request.user)
    except Partner.DoesNotExist : 
        partnerJ = None
    #applicant = ApplyP.objects.filter(partner = partnerJ)
    job = ApplyP.objects.filter(partner =request.user.id)
    #job_id = applicant.values("job")
    #jobs = Commission.objects.filter(id__in = job_id).values()
    #context = { 
       # 'jobs' :jobs ,
       # 'applicant': applicant
    #}
    applicant = ApplyP.objects.filter(partner = partnerJ).select_related('job')
    page = request.GET.get('page', 1)
	paginator = Paginator(applicant, 18)
	try:
		jjob = paginator.page(page)
	except PageNotAnInteger:
		jjob = paginator.page(1)
	except EmptyPage:
		jjob = paginator.page(paginator.num_pages)
    if not applicant :
        messages.error(request,'You have 0 Applications')
    context = { 
        'jjob' :jjob ,
        'applicant': applicant
    }
    return render(request = request , template_name = 'pat_apply.html',context=context)
    
