# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.
from builtins import print

sandwich_wish_list = ['item1', 'burito', 'mohito', 'dophamine', 'bitcoin']
sandwich_wish_list1 = ['burito', 'chemical', 'fish']
sandwich_wish_list2 = ['item2', 'salt', 'sugar', 'ingredient-232']


def func(list):
    ingredients = []
    for ingredient in list:
        ingredients.append(ingredient)
    print("Summary of the Sandwich:")
    print(ingredients)


func(sandwich_wish_list)
func(sandwich_wish_list1)
func(sandwich_wish_list2)
