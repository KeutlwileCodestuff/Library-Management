from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import admin


def Home(request):
    return render(request , 'index.html', context={"current_tab":"HOME" }  )

def BOOKS(request):
    return render(request , 'books.html', context={"current_tab":"BOOKS" }  )

def READERS(request):
    return render(request , 'readers.html', context={"current_tab":"READERS" }  )

def RETURNS(request):
    return render(request , 'returns.html', context={"current_tab":"RETURNS" }  )

def MY_BAG(request):
    return render(request , 'my_bag.html', context={"current_tab":"MY BAG" }  )

def Shopping(request):
    return HttpResponse("this is the shopping page")

def Saving(request):
    save_student = request.POST['Student name']
    return render(request , 'welcome.html', context={'Student name': save_student} )
