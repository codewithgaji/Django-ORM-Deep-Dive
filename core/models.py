from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Restaurant 
# User
# Rating

class Restaurant(models.Model):
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN', 'Indian' # The first option (CH) is what is going to be saved to the DB and the second one is a readable version for the Frontend
    CHINESE = 'CH', 'Chinese' # We shorten it intentionally
    ITALIAN = 'IT', 'Italian'
    GREEK = 'GR', 'Greek'
    MEXICAN = 'MX', 'Mexican'
    FASTFOOD = 'FF', 'Fast Food'
    OTHER = 'OT', 'Other'


  name = models.CharField(max_length=100)
  website = models.URLField(default='')
  date_opened = models.DateField()
  latitude = models.FloatField()
  longitude = models.FloatField  # To capture the location of the restaurant on google
  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices) # To choose from "TypeChoices"

  def __str__(self): # Redundant string
    return self.name # To return the name of the model field
   

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key allows you to link ONE table to another
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField() # This field allows the value to be small

  def  __str__(self):
    return f"Rating {self.rating}"


class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null = True) # Linking this to the 'Restaurant' model to reference it's "ID"
  income = models.DecimalField(max_digits=8, decimal_places=2)
  datetime = models.DateTimeField()
