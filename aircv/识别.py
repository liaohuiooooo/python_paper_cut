import pytesseract
from PIL import Image

img = 'resource/text2image.jpg'

image = Image.open(img)
code = pytesseract.image_to_string(image)
print(code)

with open('pytesseract_data.txt', 'w') as f:
    f.write(code)
