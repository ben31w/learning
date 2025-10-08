from PIL import Image

im = Image.open("PersonalPropertyTax.jpg")
print(im.format, im.size, im.mode)
im.show()