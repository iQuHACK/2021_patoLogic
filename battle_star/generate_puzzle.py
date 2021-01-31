"""Generate Battle Star puzzle using Quantum Annealing."""
from collections import defaultdict
import numpy as np

import neal
from dwave.system import LeapHybridSampler

from tools import *
from polynomials import *
from checks import *

def star_solutions(N, sample):
    """Convert :sample: into position of stars and np.array"""
    star_positions = [ind(var) for var, value in sample.items() if value == 1]
    solution = np.zeros((N, N), dtype=int)
    for (i, j) in star_positions:
        solution[i, j] = 1
    return star_positions, solution

def grid_solutions(N, sample):
    reg_colors = [indc(var) for var, value in sample.items() if value == 1]
    solution = np.zeros((N, N), dtype=int)
    for (i, j, c) in reg_colors:
        solution[i, j] = c
    return solution

def get_star_positions(sampleset, n):
    sorted_records = sorted(sampleset.record, key=lambda r: r.energy)
    variables = sampleset.variables
    record = sorted_records[n]
    sample = {x_ij: value for x_ij, value in zip(variables, record.sample)}
    energy = record.energy
    cond_1 = confirm_solution_stars(sample, regions, nstars)
    cond_2 = abs(energy-minimum_theo) < 1e-6
    print('Satisfies constraints:', cond_1)
    print('Has lowest energy:', cond_2)
    stars, solution = star_solutions(sample)
    return stars, solution, sample


def generate_stars(N: int, nstars: int, annealer="neal", num_reads=100):
    """
    Generate valid star positions on grid.
    Return a list of positions and an np.array.
    
    Annealer may be:
        1. 'neal' (simulated);
        2. 'leap' (real)."""

    g = 1
    Q = constraint_two_dont_touch(N)
    regions = [*row_regions(N), *column_regions(N)]
    for region in regions:
        Q = Q + g * region_constraint(region, nstars)
    
    if annealer == 'neal':
        sampler = neal.SimulatedAnnealingSampler()
        sampleset = sampler.sample_qubo(Q, num_reads=num_reads)
        
    elif annealer == 'leap':  # Go to DWave
        sampler = LeapHybridSampler()
        sampleset = sampler.sample_qubo(Q)
        
    else:
        raise Exception(f"Annealer {annealer} not recognized.")

        
    minimum_theo = -2 * N * nstars**2 * g
    
    valid_samples = []
    
    sorted_records = sorted(sampleset.record, key=lambda r: r.energy)
    variables = sampleset.variables
    
    for record in sorted_records:
        sample = {x_ij: value for x_ij, value in zip(variables, record.sample)}
        energy = record.energy

        cond_1 = confirm_solution_stars(sample, regions, nstars)
        cond_2 = abs(energy - minimum_theo) < 1e-6

        if not cond_1 | cond_2:
            break
            
        # Return a list of positions and an np.array.
        yield star_solutions(N, sample)

def generate_regions(N: int, nstars: int, star_positions: list, star_grid: np.array,  annealer="neal", num_reads=100):
    # Build Star Finder QUBO
    g1, g2, g3, g4 = 1, 1, 1, 1
    color_size = np.array([N]*N) #Number of sites per color
    Q_reg_1 = g1 * constraint_sum_of_stars(N, nstars, star_positions)
    Q_reg_2 = g2 * constraint_unique_color(N)
    Q_reg_3 = g3 * constraint_contiguous(N)
    Q_reg_4 = g4 * constraint_sum_of_sites(N,color_size)
    Q_reg = Q_reg_1 + Q_reg_2 + Q_reg_3 + Q_reg_4
    
    if annealer == 'neal':
        sampler = neal.SimulatedAnnealingSampler()
        sampleset = sampler.sample_qubo(Q_reg, num_reads=num_reads)
        
    elif annealer == 'leap':  # Go to DWave
        sampler = LeapHybridSampler()
        sampleset = sampler.sample_qubo(Q_reg)
        
    else:
        raise Exception(f"Annealer {annealer} not recognized.")

    upper_bound = -g1*N*nstars**2 -g2*N**2 -g4*np.sum(color_size**2)
    lower_bound = upper_bound - g3*4*N**2
      
    # Confirm Solution of Regions
    sample_star = {x(i, j): value for (i, j), value in np.ndenumerate(star_grid)}
    
    sorted_records = sorted(sampleset.record, key=lambda r: r.energy)
    variables = sampleset.variables

    for record in sorted_records:
        sample = {x_ij: value for x_ij, value in zip(variables, record.sample)}
        energy = record.energy
        grid = grid_solutions(N, sample)
        regions = [*region_lists(grid), *row_regions(N), *column_regions(N)]
        
        if confirm_solution_regions(sample_star, grid, nstars):
            yield grid

    
def generate_puzzle(N: int, nstars: int, annealer="leap", num_reads=100):
    """Generate Battle Star puzzle with NxN grid and :nstars:."""
    
    # First, find possible star placements
    star_solutions = generate_stars(N, nstars, annealer=annealer, num_reads=num_reads)
    star_pos, star_grid = first(star_solutions)
    
    # Second, find regions compatible with the star placements
    compatible_regions = generate_regions(
        N, nstars, star_pos, star_grid, annealer=annealer, num_reads=num_reads
    )
    region_grid = first(compatible_regions)
    
    return region_grid, star_grid