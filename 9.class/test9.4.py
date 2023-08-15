class Restaurant:
    def __init__ (self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"This restaurant name is {self.restaurant_name}\n")
        print(f"Cuisine type is {self.cuisine_type}\n")
    
    def open_restaurant(self):
        print("Restaurant is open !")
    
    def print_number_server(self):
        print(f"number served is {self.number_served}")
    
    def set_number_served(self,num):
        self.number_served = num
    
    def increment_number_served(self,add):
        self.number_served += add

restaurant = Restaurant('Jinitaimei','Obaby')
restaurant.number_served = 10
restaurant.print_number_server()
restaurant.set_number_served(9)
restaurant.print_number_server()
restaurant.increment_number_served(10)
restaurant.print_number_server()
