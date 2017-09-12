from django.shortcuts import render
from django.http import HttpResponse
from .models import Family


# Create your views here.
def welcome(request):
    return render(request,'family.html')
def families(request):
    families = Family.objects.all()
   
    
    context ={
        'families':families
    }  
    return render(request,'family.html',context)
 