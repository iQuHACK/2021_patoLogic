# Welcome to iQuHACK 2021!
Check out some info in the [event's repository](https://github.com/iQuHACK/2021) to get started.

Having a README in your team's repository facilitates judging. A good README contains:
* a clear title for your project,
* a short abstract,
* the motivation/goals for your project,
* a description of the work you did, and
* proposals for future work.

You can find a potential README template in [one of last year's projects](https://github.com/iQuHACK/QuhacMan).

Feel free to contact the staff with questions over our [event's slack](https://iquhack.slack.com), or via iquhack@mit.edu.

Good luck!


_Organizer's note:_ this project won the **creativity award** in iQuHACK 2020.

---

![logo](logo.png)

# Starbattle Quacklactica: Creating and Solving Star Battle Games with Quantum Annealing 

Diogo Cruz, Duarte Magano, Óscar Amaro, Sagar Pratapsi

---

Quantum annealing is a computing paradigm that has the ambitious goal of efficiently solving large-scale combinatorial optimization problems of practical importance [1,2]. In this work, we present both a generator and a solver of Star Battle games.

## Introduction

Quantum annealing has been designed to solve classical combinatorial optimization problems, with applications ranging from computer science problems, classification, quantum chemistry, machine learning, search engine ranking to protein folding. Such optimization problems require the minimization of acost function, a task that can be rephrased as finding the ground state of a classicalIsing Hamiltonian ![equation](https://latex.codecogs.com/png.latex?H_0). Many problems of practical importance, however, have costfunctions with a large number of local minima, corresponding to Ising Hamiltoniansthat are reminiscent of classical spin glasses. These characteristics makeit extremely difficult for classical algorithms to find the global minimum.

## Methods

## How to Play

Fill some cells with stars so that each row, column, and bold region contains the indicated number of stars. Stars cannot be placed in adjacent cells that share an edge or corner.

In the Menu options, you can choose to generate a new grid using a classical method, a quantum-inspired method, or using a real quantum device from D-Wave. You can also look at the solution given by a classical method, a quantum-inspired method, or using a real quantum device from D-Wave.

### Generating games

For the classical generator, the star positions and regions are random generated while taking into account some of the games rules. These games are generated until all the rules of the game are satisfied, thereby ensuring that the game grid is valid, and that there is a solution. As expected, this generator takes a long time to succeed, for bigger grids.

The quantum generator first produces a game without regions, with a distribution of stars that satisfies the games rules, by implementing a Binary Quadratic Model in a D-Wave quantum device. A subsequent Binary Quadratic Model is used to draw the regions in the game, while ensuring that the games rules are satisfied.

The quantum-inspired generator uses the same principles as the quantum one, but it is run on a quantum annealing simulator, and not a real quantum device.

## Solving games

The quantum solver uses a Binary Quadratic Model to search for a star distribution on the game's grid that satisfies all the games rules. It does so by running on a real D-Wave quantum device.

The quantum-inspired solver uses the same principles as the quantum one, but it is run on a quantum annealing simulator, and not a real quantum device.

The classical simulator uses a previously-implemented approach [3] to find a solution. It is present mainly as a debug tool.

## References



[1]Lucas, A. "Ising formulations of many NP problems." Front. Physics 2, (2014).

[2]Hauke, P., Katzgraber, H. G., Lechner, W., Nishimori, H. & Oliver, W. D. "Perspectives of quantum annealing: Methods and implementations." Rep. Prog. Phys. 83, 054401 (2020).

[3][Yadkee]. (2018, February 16). [2018-02-16] Challenge #351 [Hard] Star Battle solver [Online forum post]. Retrieved from https://www.reddit.com/r/dailyprogrammer/comments/7xyi2w/20180216_challenge_351_hard_star_battle_solver/



[1]Piotrowski, Edward W., and Jan Sładkowski. "An invitation to quantum game theory." _International Journal of Theoretical Physics_ 42.5 (2003): 1089-1099.



## Introduction

The development of quantum computing has offered revolutionary scope for many traditional areas. Game theory, a theory to study decision making in conflict situations, has been transferred into quantum version[1]. The quantum game theory is different from the traditional one in three different ways[2]:

1. The initial status is entangled
2. The initial state is superposed
3. Player strategy is quantum

These features indicate that in a quantum scenario, the definition of win and lose in a game changes fundamentally as a function of the qubit phase and rotation and the collapse of that function upon measurement.

In this project, we propose a quantum game, which is a modified version of the multi-player PacMan game. The game is a validation of quantum game theory and test quantum win strategies.


<!-- ## ToDo:
### Things we would wanna fix/implement but didn't have enough time to do


* Graphics
* More than 2 player support
* Better quantum circuit visualization
* Option to pick between real and simulated quantum simulation as opposed ot editing the source code
* Adding more gates and game mechanics to make it more fun

## Highlights:



*   In our game, the result is quantum. No one knows the results until the measurement.
*    Player can increase their probability of winning, but nothing is guaranteed.
*   During the game, two players are building a quantum circuit together. They try interfering with the result of the entangled qubits to something they desire.
*   In the game, we applied Quantum Random Number Generator to find the type and place of gates. The speeds of Quhacmans change with entangled two qubits circuit.
*   The rule and strategy are quantum. We use Bloch sphere as a win indicator. -->
