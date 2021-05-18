# 载入必要的模块
import pygame

# 保存图片
path = 'resource/text2image.jpg'

# pygame初始化
pygame.init()

# 待转换文字
text = u' This '

# 设置字体和字号
font = pygame.font.SysFont("Ubuntu", 60)

# 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
ftext = font.render(text, True, (0, 0, 0), (255, 255, 255))

pygame.image.save(ftext, path)  # 图片保存地址
