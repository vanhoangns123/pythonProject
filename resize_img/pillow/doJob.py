from PIL import Image
import os, sys

path = "C:/Users/vinhn/Google Drive/Anh Hung/youridioms/"
dirs = os.listdir( path )
print(dirs)

def resize():
    for item in dirs:
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((2400,3125), Image.ANTIALIAS)
        imResize.save(f + ' resized.png', 'PNG', quality=90)

resize()