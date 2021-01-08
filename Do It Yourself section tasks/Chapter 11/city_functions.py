# def city_country_formatted(city, country):
#     string = f"{city}, {country}"
#     return string.title()


def city_country_formatted(city, country, population=''):
    if population:
        result_string = f"{city}, {country} - {population} population"
    else:
        result_string = f"{city}, {country}"
    return result_string.title()
