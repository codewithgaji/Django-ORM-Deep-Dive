from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint # TO use pretty print


def run():
 # Deleting multiple rows in form of a Query Set
 Restaurant.objects.all().delete()
 print(connection.queries)



















#  # UPDATING & Deleting ROWS(all)
#   restaurants = Restaurant.objects.first()
#   print(restaurants.delete()) # To get rid of the data
#   print(connection.queries)

  

 




















# restaurants = Restaurant.objects.filter(name__startswith = "P")
#   print(restaurants)
#   print(restaurants.update(
#     date_opened = timezone.now() - timezone.timedelta(days=365),
#     website = "https://dummy.com"

#   ))


#  # THIS CONFIRMS THE RESTAURANT IS JUST BEING ADDED TO THE DATABASE 
#   restaurant = Restaurant() # Instantiating the Restaurant object
#   restaurant.name = "My Italian Restaurant #2"
#   restaurant.date_opened = timezone.now()
#   restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
#   restaurant.longitude = 50.5
#   restaurant.latitude = 50.2
#   restaurant.save()

#   print(connection.queries)
  



















# restaurant = Restaurant.objects.first()

#   print(restaurant.name)


#   # Updating the restaurant name
#   restaurant.name = "New Restaurant Name"

#   restaurant.save(update_fields=['name'])
#   print(connection.queries)



 # rating = Rating.objects.create(
 #   user = user,
 #   restaurant = restaurant,
 #   rating = 9
 # )
 # rating.full_clean() # allows the validators to run
 # rating.save()
 

  

 













# GET or CREATE method
  # user = User.objects.first() # The user we are applying the method on 
  # restaurant = Restaurant.objects.first() # and its restaurant

  # print(restaurant.sales.all()) # Using the "related_name" of the models

  # After instantiating the above, we now use the ".get_or_create()" method
  # And then we give necessary values to the necessary fields of the model
  # but it will check if the restaurant and user already exists
  # if yes, it won't re-create the record and just "Fetch" the data
  # but if not, it will create the record and save in the DB


  # print(Rating.objects.get_or_create(
  #   restaurant = restaurant,
  #   user = user,
  #   rating = 4
  # ))

  # pprint(connection.queries)




#  # CREATING SALES DATA

#  Sale.objects.create(
#   restaurant = Restaurant.objects.first(),
#   income = 2.33,
#   datetime = timezone.now(),
#  )

#  Sale.objects.create(
#   restaurant = Restaurant.objects.first(),
#   income = 7.33,
#   datetime = timezone.now(),
#  )

#  Sale.objects.create(
#   restaurant = Restaurant.objects.first(),
#   income = 6.33,
#   datetime = timezone.now(),
#  )


#  restaurant = Restaurant.objects.first()
#   # THIS IS A REVERSE SEARCH ON THE CHILD MODEL USING "rating_'set.all()'"
#   print(restaurant.ratings.all()) # This gets all the ratings associated with the "first" restaurant
#   # The 'ratings' attr is from the "related_name" set for the "restaurant" field with the foreign key to the parent model in the "Rating" model
#   #pprint(connection.queries)



# UPDATING PRE-EXISTING RECORDS
  # restaurant = Restaurant.objects.first()
  # print(restaurant.name)

  # restaurant.name = "La viola"
  # restaurant.date_opened = timezone.now()
  # restaurant.save()
  # pprint(connection.queries)


#  # filtering to get ratings of diff values
#   print(Rating.objects.exclude(rating__lte=3))
# #  print(Rating.objects.filter(rating=5))

#   print(connection.queries)



#  restaurant = Restaurant.objects.first()
#   user = User.objects.first() # Instance for the user
  
#   Rating.objects.create(
#     user= user, 
#     restaurant=restaurant, # Equals the "Restaurant" instance "restaurant"
#     rating = 3 # This points at the "rating" field in the model and giving the first restaurant a rating of 3
#   )

#   print("Rating created")




# TO TEST IF DATA RUNS WELL

#  print(f"Restaurant: {restaurant}")
#   print(f"User: {user}")

#   if not restaurant:
#     print("X no restaurant found")
#     return
#   if not user:
#     print("X No user found")
#     return


#print(restaurant)
# # django query set are lazily evaluated
# print(connection.queries) # This queries the DB
# restaurant = Restaurant() #Instantiating a model
# restaurant.name = 'My Italian Restaurant' # accessing the 'name' field in "Restaurant"
# restaurant.latitude = 50.5 # This are just setting some fields
# restaurant.longitude = 50.2
# restaurant.date_opened = timezone.now()
# restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
# # ".save() can also update and create a DB"
# restaurant.save() # To save the data to the DB, since it's a new record, it will create the rows and record for it
#Restaurant.objects.create( # This is to create or update a DB without needing to use the ".save()" method
#    name = "Pizza Shop",
#    date_opened = timezone.now(),
#    restaurant_type = Restaurant.TypeChoices.ITALIAN,
#    latitude = 30.6,
#    longitude = 22.4,
