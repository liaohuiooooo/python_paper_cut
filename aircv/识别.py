import pytesseract
from PIL import Image

img = '/home/liaohuiooooo/PycharmProjects/python_papercut/aircv/resource/text_image.jpg'

image = Image.open(img)
code = pytesseract.image_to_string(image)
print(code)

with open('pytesseract_data.txt', 'w') as f:
    f.write(code)
