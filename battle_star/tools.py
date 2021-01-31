"""Tools for Battle Star"""
from collections import defaultdict
import numpy as np

def first(iterable):
    return next(iter(iterable))

def x(i, j):
    """Variable label"""
    return f"x{i}_{j}"

def xc(i, j, c):
    """Variable label"""
    return f"x{i}_{j}_{c}"

def ind(var: str):
    """Return position indices from variable label"""
    i, j = var[1:].split('_')
    return (int(i), int(j))

def indc(var: str):
    """Return position indices from variable label"""
    i, j, c = var[1:].split('_')
    return (int(i), int(j), int(c))

def grid_parameters(grid, star):
    return len(grid), np.sum(star[0])

def row_regions(N):
    return [[(i, j) for j in range(N)] for i in range(N)]

def column_regions(N):
    return [[(i, j) for i in range(N)] for j in range(N)]

def region_lists(grid: np.array):
    """Lists of region indices from grid"""
    regions = defaultdict(list)
    for (i, j), r in np.ndenumerate(grid):
        regions[r].append((i, j))
    return list(regions.values())