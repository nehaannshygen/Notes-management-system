from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 
from assignment.views import dummyhome,dummyhome_student


urlpatterns=[
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('facultysignup',views.facultysignup,name='facultysignup'),
    path('login',views.login,name='login'),
    path('facultylogin',views.facultylogin,name='facultylogin'),
    path('thankyou1',views.thankyou1,name='thankyou1'),
    path('thankyou',views.thankyou,name='thankyou'),
    path('thankyou_student',views.thankyou_student,name='thankyou_student'),
    path('dummyhome_student',dummyhome_student,name='dummyhome_student'),
    path('dummyhome',dummyhome,name='dummyhome'),
    path('uploadpage', views.uploadpage,name='uploadpage'),
    path('uploadnotes/',views.uploadnotes,name='uploadnotes'),
    
    
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

