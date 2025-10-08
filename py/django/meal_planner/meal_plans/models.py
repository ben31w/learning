from django.db import models


# Create your models here.
class FoodItem(models.Model):
    """Food item model represents a food item that users can log."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
