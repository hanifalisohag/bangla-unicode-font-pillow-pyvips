# IMPORTS

import os
import pyvips
import textwrap
from PIL import *
import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# MAKE A FUNCTION

def bgoutput(filename, text):
    rendered_text, feedback = pyvips.Image.text(text,
                                                font='Siyam Rupali', fontfile='siyam.ttf',
                                                width=800, height=200,
                                                autofit_dpi=True)

    rendered_text = rendered_text.gravity('north', 1200, 1200)
    image = rendered_text.new_from_image([0, 0, 0]).bandjoin(rendered_text)
    image.write_to_file(f'{filename}.png')
    # GENERATE OUTPUT 1


text='হানিফ আলী সোহাগ'
bgoutput('new', text)
# COMBINE OUTPUT 1 WITH BACKGROUND IMAGE
img = Image.open('new.png')
b1 = Image.open('bg_img.jpg')
# img = img.resize((1000, 500))
b1.paste(img, (20, 20), mask=img)
# GENERATE FINAL OUTPUT

b1.show()
b1.save("final.png")