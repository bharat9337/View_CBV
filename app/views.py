from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *




#Returning string as response by using FBV

def fbv_strng(request):
    return HttpResponse('<h1>fbv_strng from Function based view')




#Returning string as response by class based view

class Cbvstrng(View):
    def get(self,request):
        return HttpResponse('<h1>String of CBV string')
    

    

#Rending html by FBV

def fvbhtml(request):
    return render(request,'fvbhtml.html')



#Rending html by Class Based View

class Cbvhtml(View):
    def get(self,request):
        return render(request,'Cbvhtml.html')
    
    

#Insert data by FBV through model forms   

def school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
         SFDO=SchoolForm(request.POST)
         if SFDO.is_valid():
              SFDO.save()
              return HttpResponse('school_by_fbv is done')
    return render(request,'school_by_fbv.html',d)




#Insert data by Class Based View through model forms

class SchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'SchoolByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('SchoolByCbv is done')
