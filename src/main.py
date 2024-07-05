import requests
from PIL import Image
from io import BytesIO
from colorthief import ColorThief
import matplotlib.pyplot as plt
import webcolors

from closerColor import whatColor

import colorsys





urlImg = "https://world.digimoncard.com/images/cardlist/card/EX6-056.png";

response = requests.get(urlImg)

if response.status_code== 200:
    image = Image.open(BytesIO(response.content))
    crop_box = (30,110,65,150)
    cropped_image = image.crop(crop_box) 
    
    cropped_image.show()

    cropped_image_bytes= BytesIO()
    cropped_image.save(cropped_image_bytes, format=image.format)
    cropped_image_bytes.seek(0)

    ct = ColorThief(cropped_image_bytes)
    
    pallette = ct.get_palette(color_count=2)
    """ dominant_color = ct.get_color(quality=1) """
    """ plt.imshow([[dominant_color]]) """

    
    for color in pallette:
        print(color)
        whatColor(color)

        """ print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}") """
        """  print(colorsys.rgb_to_hsv(*color)) """
        """ print(colorsys.rgb_to_hls(*color)) """


    plt.imshow([[pallette[i] for i in range(2)]])
    plt.show()
    
else:
    print('Failed Request')


