import matplotlib.pyplot as plt
import webcolors
from math import sqrt


secundary_colors ={
    'red':(255, 0, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'purple':  (128, 0, 128),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
}

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                        (g - rgb[1]) **2,
                        (b - rgb[2]) **2 ])] = color_name
       
    print('closest_color',differences)
    return differences[min(differences.keys())]


def closest_secundary_color(rgb):
    min_distance = float('inf')
    closest_color_name = None
    for color_name, color_hex in secundary_colors.items():
        r, g, b = color_hex
        distance = sqrt((r - rgb[0]) ** 2+
                        (g - rgb[1]) **2+
                        (b - rgb[2]) **2 
        )
        print('closest_secundary_color',distance)
        if distance < min_distance:
            min_distance =distance
            closest_color_name = color_name
    return closest_color_name

""" 
def closest_secundary_color(rgb):
    differences = {}
    for color_hex, color_name in secundary_colors.items():
        r, g, b = color_name
        differences[sum([(r - rgb[0]) ** 2,
                        (g - rgb[1]) **2,
                        (b - rgb[2]) **2 ])] = color_hex
       
    print('closest_color',differences)
    return differences[min(differences.keys())] """


color = (113,241,224)

def whatColor(colorTupla):
    print( closest_secundary_color(colorTupla))
    """ print( closest_color(colorTupla))
 """
    """ try:
        cname = webcolors.rgb_to_name(colorTupla)
        print(f"The color is exactly {cname}")

    except ValueError:
        cname = closest_secundary_color(colorTupla)
        print(f"The color is closest to {cname}") """

    """ plt.imshow([[colorTupla]])
    plt.show() """