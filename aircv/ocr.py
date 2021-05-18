import pytesseract
from PIL import Image

img = 'resource/text2image_sub.jpg'

image = Image.open(img)
code = pytesseract.image_to_string(image)
print(code)

with open('resource/ocr2font.txt', 'w') as f:
    f.write(code)
