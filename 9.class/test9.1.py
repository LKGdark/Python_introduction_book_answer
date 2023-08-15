class Restaurant:
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"This restaurant name is {self.restaurant_name}\n")
        print(f"Cuisine type is {self.cuisine_type}\n")
    
    def open_restaurant(self):
        print("Restaurant is open !")

my_restaurant = Restaurant('Jinitaimei','Obaby')
print(f"My restaurant name is {my_restaurant.restaurant_name}\n")
print(f"My restaurant cuisine type is {my_restaurant.cuisine_type}\n")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()