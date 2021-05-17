from PIL import Image

path = './resource/'
im1 = Image.open(path + 'lake.jpg')
im2 = Image.open(path + 'person.jpg')

out = Image.alpha_composite(im1, im2)
out.show()
