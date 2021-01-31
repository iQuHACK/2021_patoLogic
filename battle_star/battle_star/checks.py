"""Checks for validity of solutions and puzzle generation"""

import itertools as it
from .tools import *

# Puzzle solution checks

def region_criterion(sample, region: list, nstars: int):
    """Check if :region: has :nstars: in :sample:."""
    region_sum = sum(sample[x(i, j)] for (i, j) in region)
    return region_sum == nstars
    
def proximity_criterion(sample):
    """Check if stars in :sample: are not too close."""
    star_positions = [ind(var) for var, value in sample.items() if value == 1]
    bad_distances = {(0, 1), (1, 0), (1, 1)}
    for (i, j), (i_, j_) in it.combinations(star_positions, 2):
        dist = di, dj = abs(i - i_), abs(j - j_)
        if dist in bad_distances:
            return False
    return True

def confirm_solution_stars(sample, regions, nstars):
    """Check if :sample: is a solution, for given :regions: and :nstars:."""
    for region in regions:
        if not region_criterion(sample, region, nstars):
            return False

    if not proximity_criterion(sample):
        return False
    
    return True


# Puzzle generation checks

def find_neighbours(cell, region):
    """Find neighbours of given :cell: in :region:."""
    neighbours = []
    for other_cell in region:
        manhattan = abs(cell[0] - other_cell[0]) + abs(cell[1] - other_cell[1])
        if manhattan == 1:
            neighbours.append(list(other_cell))
    return neighbours
        
def connected_component(region):
    """Connected component of region that contains one of its points.
    The first point is essentially random."""
    conn = [list(region[0])] # first cell of connected component
    cell_idx = 0
    while cell_idx < len(conn): 
        cell = conn[cell_idx] 
        neighbours = find_neighbours(cell, region) # find neighbours of cell in region
        for neighbour in neighbours:
            if not neighbour in conn:
                conn.append(neighbour) # add found neighbours to connected component
        cell_idx += 1
    return conn

def is_connected(region):
    """Check if :region: is a single-connected piece."""
    conn = connected_component(region)  
    conn_set = {tuple(pos) for pos in conn}
    region_set = {tuple(pos) for pos in region}
    return conn_set == region_set

def confirm_solution_regions(sample_star, grid, nstars):
    '''Check if :grid: serves :sample_star: solution.'''
    
    regions = region_lists(grid) # do not check list/column regions 
    for region in regions:
        if not region_criterion(sample_star, region, nstars):
            return False   
        if not is_connected(region):
            return False

    return True