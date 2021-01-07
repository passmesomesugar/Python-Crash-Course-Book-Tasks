# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers_which_flow = {'Sepik': 'New Guinea', 'Ishim': 'Kazakhstan', 'Mekong': 'Asia', 'Orinoco': 'South America'}
for river, place in rivers_which_flow.items():
    print(river, 'runs through', place)
for river_name in rivers_which_flow.keys():
    print(river_name)
for country in rivers_which_flow.values():
    print(country)
# of course not all of these are countries
