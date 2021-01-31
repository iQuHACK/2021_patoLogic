"""Battle Star/Two don't touch puzzle.
Generator and solver using quantum annealing.

Annealer options:
    1. 'neal' (simulated);
    2. 'leap' (dwave computer)."""

from .generate_puzzle import generate_puzzle
from .solve_puzzle import solve_puzzle
from .plots import draw_puzzle_inline