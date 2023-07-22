from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.




def Schoolview (request):

    question = School.objects.all()
    
    context = {
        "questions": question
    }

    return render(request, 'index.html',context)

def Menusview(request, question_id):
    if request.POST:
        son = request.POST['ovoz']
        savol = menus.objects.get(id = son)
        savol.ovozlar_soni += 1
        savol.save()


    menu = menus.objects.filter(school_id = question_id)
    question = School.objects.get(id=question_id)
    context = {
        "menu":menu,
        "questions": question
    }
    return render(request, 'menu.html',context)
    

