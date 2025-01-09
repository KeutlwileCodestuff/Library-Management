from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import admin


def Home(request):
    return render(request , 'index.html', context={} )

def Shopping(request):
    return HttpResponse("this is the shopping page")

def Saving(request):
    save_student = request.POST['Student name']
    return HttpResponse("welcome " + save_student)
