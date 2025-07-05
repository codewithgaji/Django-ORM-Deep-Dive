from django import forms
from core.models import Rating, Restaurant
from django.core.validators import MinValueValidator, MaxValueValidator

class RestaurantForm(forms.ModelForm):
  class Meta:
    model = Restaurant
    fields = ('name',)
    



  # rating = forms.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)]) # We can explicitly def "validators" on the forms as well

  # class Meta:
  #   model = Rating
  #   fields = {
  #     'restaurant', 
  #     'user',
  #     'rating'
  #   }

