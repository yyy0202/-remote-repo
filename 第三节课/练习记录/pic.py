
'''
import os
for infile in pic:
 outfile = os.path.splitext(infile)[0] + ".jpg"
 if infile != outfile:
    try:
        Image.open(infile).save(outfile)
    except IOError:
        print ("cannot convert", infile)'''
from PIL import Image
pil_im = Image.open('D:\\Desktop\\py\\apple.jpg').convert('L')

pil_im.thumbnail((128,128))