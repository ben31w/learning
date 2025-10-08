guest = input("Be my guest! Enter your name: ")

filename = 'guest.txt'

# The second argument inside open(), 'w', opens the file in write mode.
#  Write mode allows you to rewrite the contents of the file using the write()
#  function. If the file you try to open in write mode doesn't exist, it will be
#  created automatically. However, if the file does exist, Python will erase its
#  contents before returning the file object (every time you open a file in 
#  write mode, you write over its existing content.) To add content to a file 
#  w/o erasing its existing content, open it in append mode using 'a'.
with open(filename, 'w') as file_object:
    file_object.write(guest)

print(f"\nCheck guest.txt, {guest}.")