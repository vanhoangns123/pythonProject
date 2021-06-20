from PIL import Image
import os, sys

path = "C:/Users/vinhn/OneDrive/Documents/pythonProject/resize_img/minify/"
dirs = os.listdir( path )
print(dirs)

def resize():
    for item in dirs:
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        # imResize = im.resize((2400,3125), Image.ANTIALIAS)
        if im.mode in ("RGBA", "P"):
            im = im.convert("RGB")
        im.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()