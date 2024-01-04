from django.urls import path

from app.views import cars_list

urlpatterns = [
    path("cars/", cars_list, name="cars_list"),
]

app_name = "app"
