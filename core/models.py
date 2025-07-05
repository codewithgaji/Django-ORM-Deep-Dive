from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError





# Create your models here.




# Restaurant 
# User
# Rating


# You can actually create a validator for the model to use
def validate_restaurant_name_begins_with_a(value):
  if not value.startswith('a'):
    raise ValidationError("Restaurant name must begin with a")




class Restaurant(models.Model):
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN', 'Indian' # The first option (CH) is what is going to be saved to the DB and the second one is a readable version for the Frontend
    CHINESE = 'CH', 'Chinese' # We shorten it intentionally
    ITALIAN = 'IT', 'Italian'
    GREEK = 'GR', 'Greek'
    MEXICAN = 'MX', 'Mexican'
    FASTFOOD = 'FF', 'Fast Food'
    OTHER = 'OT', 'Other'


  name = models.CharField(max_length=100, validators=[validate_restaurant_name_begins_with_a])
  website = models.URLField(default='')
  date_opened = models.DateField()

  latitude = models.FloatField(validators=[
    MinValueValidator(-90), MaxValueValidator(90)
  ])
  longitude = models.FloatField(validators=[
    MinValueValidator(-180), MaxValueValidator(180)
  ])  # To capture the location of the restaurant on google

  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices) # To choose from "TypeChoices"

  def __str__(self): # Redundant string
    return self.name # To return the name of the model field
   
  # This is used to check the lifecycle of a model, to see if it has been updated or deleted before
  def save(self, *args, **kwargs):
    print(self._state.adding) # This helps confirm if the model has been tampered with or not before
    super().save(*args, **kwargs)

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign key allows you to link ONE table to another
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
  rating = models.PositiveSmallIntegerField(
    validators= [
      MinValueValidator(1), MaxValueValidator(5) # Validators to constraint the ratings
    ]
  ) # This field allows the value to be small

  def  __str__(self):
    return f"Rating {self.rating}"


class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null = True, related_name='sales') # Linking this to the 'Restaurant' model to reference it's "ID"
  income = models.DecimalField(max_digits=8, decimal_places=2)
  datetime = models.DateTimeField()
