import itertools as it

from adict import adict
from tools import *

"""Penalties and constraints"""
# There is a strange problem with iterables here, all generators were converted to lists.

def constraint_two_dont_touch(N):
    """Closest neighbours should be different.
    This is a penalty of type x * y, which is 1 iff x=y=1."""

    Q = adict(int)
    positions = list(it.product(range(N-1), repeat=2))  # Exclude last row/column

    for (i, j) in positions:
        neighbours = [(i+1, j), (i, j+1), (i+1, j+1)]
        for (i_, j_) in neighbours:
            Q[x(i,j), x(i_,j_)] += 1
        Q[x(i+1, j), x(i, j+1)] += 1 # Anti-diagonal

    last_row = last_col = N-1
    for l in range(N-1):
        Q[x(last_row, l), x(last_row, l+1)] += 1
        Q[x(l, last_col), x(l+1, last_col)] += 1
        
    return Q

def region_constraint(region: list, nstars: int):
    """All points in :region: sum to :nstars:."""
    Q = adict(int)
    for (i, j) in region:
        Q[x(i,j), x(i,j)] -= 2*nstars
        for (l, p) in region:
            Q[x(i,j), x(l,p)] += 1
    return Q

def constraint_sum_of_stars(N, nstars, star_positions):
    """Sum of stars of certain color should be :nstars:"""
    Q = adict(int)
    colors = list(range(N))
    prod_pos = list(it.product(star_positions, repeat=2))
    for c in colors:
        for (i, j) in star_positions:
            Q[xc(i, j, c), xc(i, j, c)] += -2 * nstars
        for (i, j), (i_, j_) in prod_pos:
            Q[xc(i, j, c), xc(i_, j_, c)] += 1
    return Q

def constraint_sum_of_sites(N, color_size):
    """Sum of sites of certain color should be :N:"""
    Q = adict(int)
    positions = list(it.product(range(N), repeat=2))
    colors = list(range(N))
    prod_pos = list(it.product(positions, repeat=2))
    for c in colors:
        for (i, j) in positions:
            Q[xc(i, j, c), xc(i, j, c)] += -2 * color_size[c]
        for (i, j), (i_, j_) in prod_pos:
            Q[xc(i, j, c), xc(i_, j_, c)] += 1

    return Q

def constraint_unique_color(N):
    """One site should have only one color."""
    Q = adict(int)
    positions = list(it.product(range(N), repeat=2))
    colors = list(range(N))
    prod_colors = list(it.product(colors, repeat=2))
    for (i, j) in positions:
        for c in colors:
            Q[xc(i, j, c), xc(i, j, c)] += -2
        for c, c_ in prod_colors:
            Q[xc(i, j, c), xc(i, j, c_)] += 1
    return Q

def constraint_contiguous(N):
    """A color region should be contiguous.
    We favor having same-color neighbours."""
    Q = adict(int)
    positions = list(it.product(range(N-1), repeat=2))  # Exclude last row/column
    colors = list(range(N))
    for c in colors:
        for (i, j) in positions:
            Q[xc(i,j,c), xc(i+1,j,c)] += -1
            Q[xc(i,j,c), xc(i,j+1,c)] += -1

        last_row = last_col = N-1
        for l in range(N-1):
            Q[xc(last_row, l,c), xc(last_row, l+1,c)] += -1
            Q[xc(l, last_col,c), xc(l+1, last_col,c)] += -1
        
    return Q