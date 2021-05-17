
#载入必要的模块
import pygame

#pygame初始化
pygame.init()

# 待转换文字
text = u"Hello Kitty "

#设置字体和字号
font = pygame.font.SysFont("arial", 60)

#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (0, 0, 0),(255, 255, 255))

#保存图片
path = './resource/text_image.jpg'
temppath = 'hello.jpg'
pygame.image.save(ftext, temppath)#图片保存地址
