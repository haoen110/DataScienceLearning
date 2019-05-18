import pytesseract
from PIL import Image

image = Image.open("zhanshen.jpg")
string = pytesseract.image_to_string(image)
print(string)