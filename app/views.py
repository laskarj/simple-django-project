from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Car


def cars_list(request: HttpRequest) -> HttpResponse:
    car_list = Car.objects.all()
    context = {"car_list": car_list}
    return render(
        request=request,
        template_name="cars_list.html",
        context=context
    )
