from ..models import User
from django.contrib.auth import login
from ..forms import partnerRegForm,EditProfileForm , EditPartnerProfile
from django.views.generic import CreateView
from django.shortcuts import render , redirect

class partnerReg(CreateView):
    model = User
    form_class = partnerRegForm
    template_name = 'partnerReg.html'

    def get_context_data(self , **kwargs):
        kwargs['user_type'] = 'partner'
        return super().get_context_data(**kwargs)

    def form_valid(self , form):
        user = form.save()
        return redirect('account:login')

def partnerUpdate(request):
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST , instance = request.user)
        p_form = EditPartnerProfile(request.POST, instance = request.user.partner)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('account:partner_dash')
    else:
        u_form = EditProfileForm(instance = request.user)
        p_form = EditPartnerProfile(instance = request.user.partner)
     
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    return render(request , 'userUpdatePartner.html' , context)