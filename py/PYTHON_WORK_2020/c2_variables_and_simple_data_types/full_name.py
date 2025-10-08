first_name = "ada"
last_name = "lovelace"

# The string below is an "f-string." 
# The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)

# F-strings were first introduced in Python 3.6. If you're using Python 3.5 or earlier, you'll need to use the format() method 
# rather than f syntax. To use format(), list the variables you want to use in the string inside the parenthesis following format.
# Each variable is referred to by a set of braces; the braces will be filled by the values of the variables listed in format().
full_name = "{} {}".format(first_name, last_name)
print(full_name)

message = "Hello, {}!".format(full_name.title())
print(message)