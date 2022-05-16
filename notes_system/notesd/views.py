

import mysql.connector
from django.shortcuts import render, redirect
from django.http import HttpResponse
from operator import itemgetter

from signup.models import notes

def search(request):
    query1 = request.GET.get('query1')
    query2 = request.GET.get('query2')
    #allNotes = notes_table.objects.all()
    allNotes = notes.objects.filter(coursecode__icontains=query1,coursename__icontains=query2)
    params = {'allNotes':allNotes,'query1':query1,'query2':query2}
    return render(request,'search.html',params)
    #return HttpResponse('This is Search')

# Create your views here.

def SearchPage(request):
    return render(request,'SearchPage.html')

#def SearchPage(request):
    #con1=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="notes")
    #cursor1=con1.cursor()
    #con2=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="notes")
    #cursor2=con2.cursor()
    #sql_ccode="select coursecode from notes_table"
    #sql_ccname="select coursename from notes_table"
    #cursor1.execute(sql_ccode)
    #cursor2.execute(sql_ccname)
    #r=[]
    #p=[]
    #for i in cursor1:
        #r.append(i)
    #for j in cursor2:
        #p.append(j)
        
    #res1=list(map(itemgetter(0),r))
    #res2=list(map(itemgetter(0),p))

    #if request.method=="POST":
        #data=request.POST.get
        #coursecode=data('coursecode',False)
        #coursename=data('coursename',False)
        #i=1
        #k=len(res1)
        #while i<k:
            #if res1[i]==coursecode and res2[i]==coursename:
                #return redirect(request,'searchresult') 
    #else:     
        #return render(request,'SearchPage.html')

#def SearchPage(request):
    #ccode = request.GET['query']
    #cname = request.GET['query']
    #tname = request.GET['query']
    #notes_tables = notes_table.objects.filter(coursecode__icontains=ccode,coursename__icontains=cname,topicname__icontains=tname)
    #notes_tables = notes_table.objects.filter(coursecode__icontains=ccode)
    #params = {'notes_tables': notes_tables, 'coursecode':ccode,'coursename':cname,'topicname':tname}
    #params = {'notes_tables': notes_tables, 'coursecode':ccode}
    #return render(request, 'SearchPage.html', params)

#def searchresult():
   # return render ('searchresult.html')

    
    