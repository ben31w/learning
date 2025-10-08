from restaurant import Restaurant

golden_china = Restaurant('golden china', 'chinese', 1000)
brg = Restaurant('blue ridge grill', 'american')
outback = Restaurant('outback steakhouse', 'australian', 2000)

brg.set_number_served(2000)
outback.increment_number_served(1000)

golden_china.describe_restaurant()
brg.describe_restaurant()
outback.describe_restaurant()