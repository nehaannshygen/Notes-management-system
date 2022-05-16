from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import assignment_details,assignment_answer

from signup import views
import mysql.connector
from operator import itemgetter


# Create your views here.
def AssignmentFaculty(request):
    if request.method=='POST':
        data=request.POST.get
        registration=data('registration',False)
        class_code=data('class_code',False)
        year=data('year',False)
        instructions=data('instructions',False)
        upload=request.FILES['upload']
        ins=assignment_details(registration=registration,class_code=class_code,year=year,instructions=instructions,upload=upload)
        ins.save()
        print("data has been saved")
        print(upload.name)
        print(upload.size)
        return redirect('thankyou')

    if request.method == 'GET':
        return render(request,'AssignmentFaculty.html')


def AssignmentStudent(request):
    query_results = assignment_details.objects.all()
    if request.method=='POST': 
        
            student_registration = request.POST.get('student_registration',False)
            class_code = request.POST.get('class_code',False)
            try:
                upload_answer=request.FILES['upload_answer']
                
            except:
                return render(request,'AssignmentStudent.html')
            ins=assignment_answer(student_registration=student_registration,upload_answer=upload_answer,class_code=class_code)
            ins.save()
            print("data has been saved")
            print(upload_answer.name)
            print(upload_answer.size)
            return redirect('thankyou_student')
        

    
    if request.method == 'GET':
        return render(request,'AssignmentStudent.html',{'assignments':query_results})


def dummyhome(request):
    return render(request, 'dummyhome.html')

def Assignmentview(request):
    
    query_results = assignment_answer.objects.all()
    return render(request, 'Assignmentview.html',{'assignments_answers':query_results})


def dummyhome_student(request):
    return render(request, 'dummyhome_student.html')