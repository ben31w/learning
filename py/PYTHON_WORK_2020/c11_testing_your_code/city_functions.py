def city_country(city, country, population=''):
    """
    Given a city and a country, return a string in 'City, Country' format.
    If the function is given a population, return a string in 
    'City, Country - population xxx' format.
    """
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"