# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings
print("Comparing random_string and 'another string for comparison':")
random_string = "truly random string "
print(random_string == "another string for comparison")
print()

# • Tests using the lower() method
string = "SoMe strIng wiTh sTatEmEnt, Hi to JAVA uSers"
print("Comparing 'SoMe strIng wiTh sTatEmEnt, Hi to JAVA uSers' with 'some string with statement, hi to java users':")
print(string.lower() == "some string with statement, hi to java users")
print()

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
my_bank_account = 100000
print("My bank account statement is:", my_bank_account)
print("My bank account statement is not 100000:", my_bank_account != 100000)
print("My bank account statement is 762:", my_bank_account == 762)
print("My bank account is more than thousand:", my_bank_account > 1000)
print("My bank account is less than thousand:", my_bank_account < 1000)
print("My bank account is more or equal to hundred thousand:", my_bank_account >= 100000)
print("My bank account is equal to million:", my_bank_account == 1000000)
print("My bank account is less or equal to million:", my_bank_account <= 1000000)
print()

# • Tests using the and keyword 'and' the 'or' keyword
age = 21
print("Age is:", age)
print("Age value is more than one and more than two:")
print(age > 1 and age > 2)
print("Age value is more than thirty or more than fifteen:")
print(age > 30 or age > 15)
print()

# • Test whether an item is in a list
list_of_items = ["sword", "glove", "dragon's tail", "mana bottle", "some stone I've found in troll cave",
                 "elvish weapon", "aghanim scepter"]
print("'Aghanim scepter',  is in my list of items: ", 'aghanim scepter' in list_of_items)
# • Test whether an item is not in a list
print("I've got some 'elder scrolls' in my list of items: ", 'elder scrolls' in list_of_items)
