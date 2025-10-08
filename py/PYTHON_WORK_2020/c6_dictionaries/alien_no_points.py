alien_0 = {'color': 'green', 'speed': 'slow'}

# If you try to access alien_0['points'], you'll get a KeyError because the key
# doesn't exist. Instead, use the get() method by passing a key as the first
# argument and an optional return value for when the key doesn't exist as the 
# second argument.
point_value = alien_0.get('points')
print(point_value)

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)