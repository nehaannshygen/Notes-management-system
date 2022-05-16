from os import name
from django.db.models import fields
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signup_table
from .models import faculty_signup
import mysql.connector
from operator import itemgetter
from notesd import *
from assignment import views
from .models import notes
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=="POST":
        data=request.POST.get
        firstname=data('firstname',False)
        lastname=data('lastname',False)
        yearofjoining=data('yearofjoining',False)
        registration=data('registration',False)
        pwd=data('pwd',False)
        #rpwd=data('rpwd',False)
        #if pwd==rpwd:
        ins=signup_table(firstname=firstname,lastname=lastname,yearofjoining=yearofjoining,registration=registration,pwd=pwd)
        ins.save()
        print("data has been saved")
        return redirect('notesd/SearchPage')
 
    else:     
        return render(request,'signup.html')

def facultysignup(request):
    if request.method=="POST":
        data=request.POST.get
        firstname=data('firstname',False)
        lastname=data('lastname',False)
        coursecode=data('coursecode',False)
        registration=data('registration',False)
        classnumber=data('classnumber',False)
        pwd=data('pwd',False)
        #rpwd=data('rpwd',False)
        #if pwd==rpwd:
        ins=faculty_signup(firstname=firstname,lastname=lastname,coursecode=coursecode,registration=registration,classnumber=classnumber,pwd=pwd)
        ins.save()
        print("data has been saved")
        return redirect('uploadpage')
 
    else:     
        return render(request,'facultysignup.html')


def login(request):
    con1=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="notes")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="notes")
    cursor2=con2.cursor()
    sql_reg="select registration from signup_signup_table"
    sql_pwd="select pwd from signup_signup_table"
    cursor1.execute(sql_reg)
    cursor2.execute(sql_pwd)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
        
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))

    if request.method=="POST":
        data=request.POST.get
        registration=data('registration',False)
        pwd=data('pwd',False)
        i=0
        k=len(res1)
        while i<k:
            if res1[i]==registration and res2[i]==pwd:
                return redirect('notesd/SearchPage')
            i = i+1
        return HttpResponse('<h1 style="font-size:30px">Wrong Registration no: or password</h1>')    
    else:     
        return render(request,'login.html')

def facultylogin(request):
    con1=mysql.connector.connect(host="localhost",user="root",password="mysql123",database="notes")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",password="mysql123",database="notes")
    cursor2=con2.cursor()
    sql_reg="select registration from signup_faculty_signup"
    sql_pwd="select pwd from signup_faculty_signup"
    cursor1.execute(sql_reg)
    cursor2.execute(sql_pwd)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
        
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))

    if request.method=="POST":
        data=request.POST.get
        registration=data('registration',False)
        pwd=data('pwd',False)
        i=0
        k=len(res1)
        while i<k:
            if res1[i]==registration and res2[i]==pwd:
                return redirect('uploadpage')
            i=i+1
        return HttpResponse('<h1 style="font-size:30px">Wrong Registration no: or password</h1>')
    else:     
        return render(request,'facultylogin.html')

def thankyou(request):
    # here
    return render(request,'thankyou.html')

def thankyou1(request):
    # here
    return render(request,'thankyou1.html')

def thankyou_student(request):
    return render(request,'thankyou_student.html')

def uploadpage(request):
    return render(request, 'uploadpage.html')

def uploadnotes(request):
    if request.method=='POST':
        context={}
        data=request.POST.get
        registration= data('registration',False)
        facultyname=data('facultyname',False)
        coursecode=data('coursecode',False)
        coursename=data('coursename',False)
        topicname=data('topicname',False)
        pdf=request.FILES['pdf']
        ins=notes(registration=registration,facultyname=facultyname,coursecode=coursecode,coursename=coursename,topicname=topicname,pdf=pdf)
        ins.save()
        print("data has been saved")
        return redirect('thankyou1')
    else:    
        return render(request, 'uploadnotes.html')

'''
def uploadasg(request):
    if request.method=='POST':
        context={}
        data=request.POST.get
        facultyname=data('facultyname',False)
        coursecode=data('coursecode',False)
        coursename=data('coursename',False)
        topicname=data('topicname',False)
        pdf=request.FILES['pdf']
        notes(facultyname=facultyname,coursecode=coursecode,coursename=coursename,topicname=topicname,pdf=pdf).save()
        print("data has been saved")
        return redirect('thankyou')
    else:    
        return render(request, 'uploadasg.html')
'''

