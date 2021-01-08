# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name:  {self.restaurant_name}")
        print(f"Cuisine type:  {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant("Moe's", "Fast Food")
restaurant_2 = Restaurant("Joe's", "Fast & Cheap Food")
restaurant_3 = Restaurant("Krusty Krabs", "Sea Food")

restaurant_1.open_restaurant()
print(f"{restaurant_1.cuisine_type}")
print(f"{restaurant_1.restaurant_name}")
print()

restaurant_2.open_restaurant()
print(f"{restaurant_2.cuisine_type}")
print(f"{restaurant_2.restaurant_name}")
print()

restaurant_3.open_restaurant()
print(f"{restaurant_3.cuisine_type}")
print(f"{restaurant_3.restaurant_name}")
print()
