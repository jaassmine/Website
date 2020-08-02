from django.urls import path ,include

from .views import candidateViwe , partnerView,accounts

# from . import views 

app_name = 'account'
urlpatterns = [
    # path('' , main.homepage , name = 'homepage'),
    path('login/' , accounts.loginpage , name = 'login'),
    path('loginp/' , accounts.loginpageP , name = 'loginp'),
    path('logout/' , accounts.logoutuser, name='logout'),
    path('candidateReg/', candidateViwe.candidateReg.as_view() , name = 'candidateReg'),
    path('candidateDash/', accounts.candidate_dash , name = 'candidate_dash'),
    path('partnerDash/', accounts.partner_dash , name = 'partner_dash'),
    path('partnerreg/', partnerView.partnerReg.as_view() , name = 'partnerReg'),
    path('patapply/', accounts.patapply , name = 'patapply'),
    path('candapply/', accounts.candapply , name = 'candapply'),
    path('updateCandidate/', candidateViwe.candidateUpdate , name = 'updateCandidate'),
    path('updatePartner/', partnerView.partnerUpdate , name = 'partnerupdate'),
]
