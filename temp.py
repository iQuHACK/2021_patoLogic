import dimod

exactsolver = dimod.ExactSolver()

Q = {(0,0): -1, (1,1): -1, (0,1): 2}

results = exactsolver.sample_qubo(Q)

# print the results
for sample, energy in results.data(['sample','energy']):
    print(sample, energy)