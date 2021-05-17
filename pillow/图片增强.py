
from PIL import  ImageEnhance
from PIL import  Image
import os

url = './resource/图像增强/pic'
pic_url = url+'.jpg'
pic = Image.open(pic_url)

enhancer = ImageEnhance.Sharpness(pic)

for i in range(20):
    factor = i/4.0
    pic__url = url + str(factor) +'.jpg'
    enhancer.enhance(factor).save(pic__url)