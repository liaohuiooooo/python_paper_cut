
#载入必要的模块
import pygame

#pygame初始化
pygame.init()

# 待转换文字
text = u"  2  "

#设置字体和字号
font = pygame.font.SysFont("arial", 60)

#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (0, 0, 0),(255, 255, 255))

#保存图片
pygame.image.save(ftext, "./resource/text_image.jpg")#图片保存地址