from django.shortcuts import render
from django.http import HttpResponse

from app.models import Car

def cars_list(request):
    return HttpResponse("Car List!")
