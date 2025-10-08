def describe_city(city, country='germany'):
    """States a city and the country it is located in."""
    print(f"{city.title()} is located in {country.title()}.")

def city_country(city, country):
    """Given a city and its country, returns the two words in City, Country format."""
    return f"{city.title()}, {country.title()}"