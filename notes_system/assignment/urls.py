from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

app_name = 'assignment'
 
urlpatterns=[
    path('dummyhome',views.dummyhome,name='dummyhome'),
    path('AssignmentFaculty',views.AssignmentFaculty,name='AssignmentFaculty'),
    path('Assignmentview',views.Assignmentview,name='Assignmentview'),
    path('dummyhome_student',views.dummyhome_student,name='dummyhome_student'),
    path('AssignmentStudent',views.AssignmentStudent,name='AssignmentStudent'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

