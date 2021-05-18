from aircv import find_template, imread
from PIL import Image, ImageEnhance

img_src = \
    '/resource/origin.jpeg'
img_obj = \
    'resource/text_image.jpg'

out_img_name = \
    'resource/output.png'


def matchImg(imgsrc, imgobj, confidence=0.2):
    """
        图片对比识别imgobj在imgsrc上的相对位置（批量识别统一图片中需要的部分）
    :param imgsrc: 原始图片路径(str)
    :param imgobj: 待查找图片路径（模板）(str)
    :param confidence: 识别度（0<confidence<1.0）
    :return: None or dict({'confidence': 相似度(float), 'rectangle': 原始图片上的矩形坐标(tuple), 'result': 中心坐标(tuple)})
    """
    imsrc = imread(imgsrc)
    imobj = imread(imgobj)

    match_result = find_template(imsrc, imobj, confidence)
    # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    return match_result


def cutImg(imgsrc: object, out_img_name: object, coordinate: object) -> object:
    """
        根据坐标位置剪切图片
    :rtype: object
    :param imgsrc: 原始图片路径(str)
    :param out_img_name: 剪切输出图片路径(str)
    :param coordinate: 原始图片上的坐标(tuple) egg:(x, y, w, h) ---> x,y为矩形左上角坐标, w,h为右下角坐标
    :return:
    """
    image = Image.open(imgsrc)
    region = image.crop(coordinate)
    region = ImageEnhance.Contrast(region).enhance(1.5)
    region.save(out_img_name)



pos = matchImg(img_src, img_obj)

print(pos)

message = str(pos)

with open("位置识别结果.txt", 'w') as f:
    f.write(message)


left_position = pos['rectangle'][0]
right_position = pos['rectangle'][3]
position = left_position + right_position
print(position)
print(type(position))

out = cutImg(img_src, out_img_name, position)


