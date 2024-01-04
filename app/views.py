from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from app.models import Car

def cars_list(request: HttpRequest) -> HttpResponse:
    car_list = Car.objects.all()
    context = {"car_list": car_list}
    return render(
        request=request,
        template_name="cars_list.html",
        context=context
    )
