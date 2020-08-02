from django.shortcuts import render , redirect
from ..forms import candidateRegForm , EditProfileForm , EditCandidateProfile
from ..models import User , Candidate
from django.views.generic import CreateView , UpdateView

# from django.contrib.auth import authenticate , login , logout


class candidateReg(CreateView):
    model = User
    form_class = candidateRegForm
    template_name = 'candidateReg.html'

    def get_context_data(self , **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)
    
    def form_valid(self , form):
        user = form.save()
        return redirect('account:login')  
        # return redirect('account:home')


def candidateUpdate(request):
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST , instance = request.user)
        c_form = EditCandidateProfile(request.POST, instance = request.user.candidate)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            return redirect('account:candidate_dash')
    else:
        u_form = EditProfileForm(instance = request.user)
        c_form = EditCandidateProfile(instance = request.user.candidate)
     
    context = {
        'u_form' : u_form,
        'c_form' : c_form
    }
    
    return render(request , 'userUpdateProfile.html' , context)

