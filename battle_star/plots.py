import numpy as np
import matplotlib.pyplot as plt

from tools import *

def grid_solutions(N, sample):
    reg_colors = [indc(var) for var, value in sample.items() if value == 1]
    solution = np.zeros((N, N), dtype=int)
    for (i, j, c) in reg_colors:
        solution[i, j] = c
    return solution

def draw_puzzle(grid, star):
    fig, ax = plt.subplots()
    mat = ax.imshow(grid, cmap='GnBu', interpolation='nearest')
    for x in range(star.shape[0]):
        for y in range(star.shape[1]):
            if star[x,y] == 1:
                ax.annotate("*", xy=(y, x), horizontalalignment='center', verticalalignment='center',size=30)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
def sample_to_plot(N, sample_star, sample_reg=None):
    if sample_reg is None:
        grid = np.zeros((N, N), dtype=int)
        _, solution = star_solutions(sample_star)
    else:
        grid = grid_solutions(N, sample_reg)
        solution = sample_star
    draw_puzzle(grid, solution)