import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
from matplotlib.cbook import get_sample_data
import matplotlib.image as mpimg

from .tools import *

def draw_puzzle(grid, star):
    my_dpi = 100
    plotsize = 773
    fig, ax = plt.subplots(figsize=(plotsize/my_dpi, plotsize/my_dpi), dpi=my_dpi)
    mat = ax.imshow(grid, cmap='Set3', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.savefig('puzzle.png', bbox_inches='tight',pad_inches = 0)
    arr_img = plt.imread('battle_star/duck1.png')
    imagebox = OffsetImage(arr_img, zoom=0.6)
    for x in range(star.shape[0]):
        for y in range(star.shape[1]):
            if star[x,y] == 1:
                ab = AnnotationBbox(imagebox, (y, x),  xycoords='data', frameon=False)
                ax.add_artist(ab)
    plt.savefig('solution.png', bbox_inches='tight',pad_inches = 0,dpi=my_dpi)
    plt.close(fig)
    plt.show()
    
def draw_puzzle_inline(grid, star):
    my_dpi = 100
    plotsize = 773
    fig, ax = plt.subplots(figsize=(plotsize/my_dpi, plotsize/my_dpi), dpi=my_dpi)
    mat = ax.imshow(grid, cmap='Set3', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.savefig('puzzle.png', bbox_inches='tight',pad_inches = 0)
    arr_img = plt.imread('battle_star/duck1.png')
    imagebox = OffsetImage(arr_img, zoom=0.6)
    for x in range(star.shape[0]):
        for y in range(star.shape[1]):
            if star[x,y] == 1:
                ab = AnnotationBbox(imagebox, (y, x),  xycoords='data', frameon=False)
                ax.add_artist(ab)
    plt.show()
    