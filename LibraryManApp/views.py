from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import admin


def Home(request):
    return render(request , 'templates.index.html', context={} )