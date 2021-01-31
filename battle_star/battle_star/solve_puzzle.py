"""Solve Battle Star puzzle using Quantum Annealing."""
from collections import defaultdict
import numpy as np

import neal
from dwave.system import LeapHybridSampler

from .tools import *
from .polynomials import *
from .checks import *

def star_solutions(N, sample):
    """Convert :sample: into position of stars and np.array"""
    star_positions = [ind(var) for var, value in sample.items() if value == 1]
    solution = np.zeros((N, N), dtype=int)
    for (i, j) in star_positions:
        solution[i, j] = 1
    return star_positions, solution

def theoretical_minimum(N, nstars, γ):
    '''Predicted energy of exact solution'''
    return -3 * N * nstars**2 * γ

def solve_puzzle(N, nstars, grid, annealer="neal", num_reads=10):
    Q = constraint_two_dont_touch(N)

    regions = [
        *region_lists(grid),
        *row_regions(N),
        *column_regions(N),
    ]

    g = 1
    for region in regions:
        Q = Q + g * region_constraint(region, nstars)


    # Create Sampler
    
    if annealer == 'neal':
        sampler = neal.SimulatedAnnealingSampler()
        sampleset = sampler.sample_qubo(Q, num_reads=num_reads)
        
    elif annealer == 'leap':  # Go to DWave
        sampler = LeapHybridSampler()
        sampleset = sampler.sample_qubo(Q)
        
    else:
        raise Exception(f"Annealer {annealer} not recognized.")
        

    minimum_energy = theoretical_minimum(N, nstars, g)

    sorted_records = sorted(sampleset.record, key=lambda r: r.energy)
    variables = sampleset.variables
    for record in sorted_records:
        sample = {x_ij: value for x_ij, value in zip(variables, record.sample)}
        energy = record.energy
        
        is_solution = confirm_solution_stars(sample, regions, nstars)
        
        if is_solution:
            _, solution = star_solutions(N, sample)
            return solution