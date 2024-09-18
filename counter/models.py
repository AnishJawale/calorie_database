from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values
    name = models.CharField(max_length=100)
    calories = models.CharField(max_length=100, default="Not available")  # String since it's not a number in the response
    fat_total_g = models.FloatField(null=True, blank=True)
    fat_saturated_g = models.FloatField(null=True, blank=True)
    protein = models.CharField(max_length=100, default="Not available")  # String since it's not a number in the response
    sodium_mg = models.FloatField(null=True, blank=True)
    potassium_mg = models.FloatField(null=True, blank=True)
    cholesterol_mg = models.FloatField(null=True, blank=True)
    carbohydrates_total_g = models.FloatField(null=True, blank=True)
    fiber_g = models.FloatField(null=True, blank=True)
    sugar_g = models.FloatField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
