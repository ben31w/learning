from django.db import models


# Create your models here.
class Pizza(models.Model):
    """
    Pizza model represents a type of pizza we serve.
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """
    Topping model represents a topping we offer.
    A topping is tied to a pizza.
    """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} ({self.pizza})"
