cities = {
    'washington': {
        'country': 'united states',
        'population': 705_749,
        'fact': "Washington's black population outnumbers its white population."
    },
    'ottawa': {
        'country': 'canada',
        'population': 923_243,
        'fact': "Ottawa is located in Ontario, but it borders Quebec." 
    },
    'mexico city': {
        'country': 'mexico',
        'population': 8_918_653,
        'fact': "Mexico City is the largest city in North America by population."
    }
}

for city, city_info in cities.items():
    print(city.title())
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fun Fact: {city_info['fact']}\n")