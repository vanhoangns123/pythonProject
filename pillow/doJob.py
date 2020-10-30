from PIL import Image
import os, sys

path = "/Users/vinhn/Desktop/fix2/"
dirs = os.listdir( path )
print(dirs)

def resize():
    for item in dirs:
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((3300,4600), Image.ANTIALIAS)
        imResize.save(f + ' resized.png', 'PNG', quality=90)

resize()