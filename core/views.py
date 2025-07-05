from django.shortcuts import render
from .forms import RestaurantForm

# Create your views here.

def index(request):
  if request.method == 'POST': # This is  a "POST" request
    form = RestaurantForm(request.POST or None) # Instantiate it
    if form.is_valid(): # Validate it
      print(form.cleaned_data) # This prints to the terminal
      # form.save()
    else:
      return render(request, 'index.html', {'form': form})
    
  context = {'form': RestaurantForm()}
  return render(request, 'index.html', context)



