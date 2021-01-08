# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
cities = {'nagoya': {'country': 'japan', 'population': '2,327,557',
                     'fact': 'Possible name origin is the adjective nagoyaka (なごやか), meaning peaceful.'},
          'minna': {'country': 'nigeria', 'population': '304,113',
                    'fact': 'Settlement in the area dates back to about 47,000–37,000 years ago.'},
          'seosan': {'country': 'korea', 'population': '175,000',
                     'fact': 'Famous Korean singer, actor Rain was born in here.'}
          }
for city, info in cities.items():
    print(
        f"{city.title()} is located in {info['country'].title()}, has population of {info['population']}; fact: {info['fact']}")
