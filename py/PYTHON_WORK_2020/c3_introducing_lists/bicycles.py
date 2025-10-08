# In Python, square brackets indicate a list, and individual elemesnts in the list are separated by commas.
# Example of a list containing types of bicycles:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3] + "\n")

print(bicycles[-1].title()) # putting -1 as the index will return the last element of the list
print(bicycles[-2].title()) # putting -2 as the index will return the second to last element of the list
print(bicycles[-3].title()) # etc.
print(bicycles[-4].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)