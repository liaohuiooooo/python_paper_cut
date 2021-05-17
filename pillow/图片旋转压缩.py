from PIL import Image
import glob,os


size = 200, 128

for file in glob.glob("resource/图片旋转压缩/*.jpg"):
    # file, ext = os.path.splitext(file)
    with Image.open(file) as im:
        im.thumbnail(size)
        im.save(file + "_thumbnail", "JPEG")
        im.rotate(90).save(file + "_rotate","JPEG")

