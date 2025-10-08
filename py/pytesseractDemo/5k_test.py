import pytesseract
from PIL import Image

img = Image.open("Mile-paces-1500.png")

# text = pytesseract.image_to_string(img)
# print(text)

table_str = pytesseract.image_to_string(img, config="--psm 6")
print(table_str)