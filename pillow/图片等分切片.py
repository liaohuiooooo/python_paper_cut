from PIL import Image

# 切分个数 = num*mun
num = 3

im = Image.open('./resource/图片等分切割/1.jpeg')

weight = int(im.size[0] // num)
height = int(im.size[1] // num)

# PIL之image模块crop方法切割图片参数介绍
#
# crop(left,top,right,bottom)
#
# left:距离左边边框的位置,
#
# top:距离顶部的位置；
#
# right:距离左边的位置，需要比left大，
#
# bottom,距离顶部的位置，需要比top大

for i in range(num):
    for j in range(num):
        # lefg top right bottom
        box = (weight * i, height * j, weight*(i+1), height*(j+1))
        region = im.crop(box)
        name = str(i) + str(j)
        # print(name)
        fp = './resource/图片等分切割/%s.jpeg' % name
        print(fp)
        region.save(fp, format=None)