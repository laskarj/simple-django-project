from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=63)
    brand = models.CharField(max_length=63)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.brand}({self.model})"
