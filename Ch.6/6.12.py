# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

cities = {'nagoya': {'country': 'japan', 'population': '2,327,557',
                     'fact': 'Possible name origin is the adjective nagoyaka (なごやか), meaning peaceful.',
                     'message': 'You should visit'},
          'minna': {'country': 'nigeria', 'population': '304,113',
                    'fact': 'Settlement in the area dates back to about 47,000–37,000 years ago.',
                    'message': 'You should visit'},
          'seosan': {'country': 'korea', 'population': '175,000',
                     'fact': 'Famous Korean singer, actor Rain was born in here.', 'message': 'You should visit'}
          }
for city, info in cities.items():
    print(
        f"{city.title()} is located in {info['country'].title()}, has population of {info['population']}; fact: {info['fact']}")
    print(f"{info['message']} {city.title()}")
