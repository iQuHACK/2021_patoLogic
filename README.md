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

# Quack Battle: Creating and Solving Star Battle Games with Quantum Annealing 

Diogo Cruz, Duarte Magano, Óscar Amaro, Sagar Pratapsi

---

Quantum annealing is a computing paradigm that has the ambitious goal of efficiently solving large-scale combinatorial optimization problems of practical importance [1,2]. In this work, we present both a generator and a solver of Star Battle games.

## Introduction

Quantum annealing has been designed to solve classical combinatorial optimization problems, with applications ranging from computer science problems, classification, quantum chemistry, machine learning, search engine ranking to protein folding. Such optimization problems require the minimization of acost function, a task that can be rephrased as finding the ground state of a classicalIsing Hamiltonian ![equation](https://latex.codecogs.com/png.latex?H_0). Many problems of practical importance, however, have costfunctions with a large number of local minima, corresponding to Ising Hamiltoniansthat are reminiscent of classical spin glasses. These characteristics makeit extremely difficult for classical algorithms to find the global minimum.

## Methods

### Generating games

For the classical generator, the star positions and regions are random generated while taking into account some of the games rules. These games are generated until all the rules of the game are satisfied, thereby ensuring that the game grid is valid, and that there is a solution. As expected, this generator takes a long time to succeed, for bigger grids.

The quantum generator first produces a game without regions, with a distribution of stars that satisfies the games rules, by implementing a Binary Quadratic Model in a D-Wave quantum device. A subsequent Binary Quadratic Model is used to draw the regions in the game, while ensuring that the games rules are satisfied.

The quantum-inspired generator uses the same principles as the quantum one, but it is run on a quantum annealing simulator, and not a real quantum device.

## Solving games

The quantum solver uses a Binary Quadratic Model to search for a star distribution on the game's grid that satisfies all the games rules. It does so by running on a real D-Wave quantum device.

The quantum-inspired solver uses the same principles as the quantum one, but it is run on a quantum annealing simulator, and not a real quantum device.

The classical simulator uses a previously-implemented approach [3] to find a solution. It is present mainly as a debug tool.

## How to play

In the Menu options, you can choose to generate a new grid using a classical method, a quantum-inspired method, or using a real quantum device from D-Wave.

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

## Basic principles

The two-qubit state is initialized at entangled states psi = a |01>+b|10>. Each player will collect certain gates during the game (either acting on both qubits or ). Effectively, the prefactor a and b change dynamically during the game. There are measurement gates available for the player to pick up as well. Upon one-shot measurement, the quantum state collapses to player one getting |0> and player two getting |1> or the opposite. Whoever gets |0> is the winner!

The evaluation of the quantum circuit generating from the gaming processes are conducted by qiskit package.

## Elements and rules


Two players in the game are gambling the final output of a quantum circuit with two entangled qubits. One can gain an advantage to win by eating beans to modify the Bloch sphere of their qubit. After measurement, the entangled qubits collapse to classical states, determines the game result.

Below is the explanation of essential elements:



*   Maze: The map is the same as the conventional PacMan game. Players can move at the route divided by walls.
*   Pac-man: Two players are playing as PacMan in the game. The PacMan can move, eat beans/gates and avoid being caught by ghosts.
*   Ghost: Ghost is automatically generated by the game to catch the PacMans in the game. The ghosts are moving gates. Once the ghost encountering one PacMan, Rx(-pi/9) gate is applied on one's qubit, and Rx(pi/9) gate is applied on another's qubit.
*   Beans: Players will eat the beans in the route they move. In this game, one bean means a rotation gate of Rx(pi/36) in PacMan's qubit.
*   Gates: Gates are randomly added in the beans to change the final quantum circuit. We used a separate quantum circuit to generate random numbers to assign gates in the maze.
    *   S gate: a separate 2 qubit quantum circuit to randomly generate |00> and |11> states. If |00> is measured, the hit PacMan speeds up, the other PacMan slows down. If If |11> is measured, the hit PacMan slows, the other PacMan speed up.
    *   Swap gate: The qubits of two players swap.
    *   H gate: adding Hadamard gate in the circuit.
*   Measure gate: Once PacMan hits measure gate, the game ends.

Basic Rules:



*   The game starts with initial maze and two players at the same place. Two players separately control two PacMan in the maze.
*   PacMan can move, eat beans, eat gates, hit ghosts and eat measure gate.
*   The two Bloch spheres on the side of maze represent the wave functions of two players.
*   Player 1 uses WSAD and player 2 uses up down left right arrow key to control their PACMan

Advanced Strategies:



*   Player should keep the pointer close to the win state to have the largest winning probability. Eating more beans after pointer reach the highest position will lower it down.
*   Try to lower down the pointer of your opponent
*   Finish/Measure the game when you have advantage (But moving there may eat more beans, worth it?)

## Demonstrations:

The GitHub repository link is [https://github.com/tareqdandachi/quhackman](https://github.com/tareqdandachi/quhackman).

[1]Piotrowski, Edward W., and Jan Sładkowski. "An invitation to quantum game theory." _International Journal of Theoretical Physics_ 42.5 (2003): 1089-1099.

[2]Quantum Game Theory, Wikipedia. [https://en.wikipedia.org/wiki/Quantum_game_theory](https://en.wikipedia.org/wiki/Quantum_game_theory)

## ToDo:
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
*   The rule and strategy are quantum. We use Bloch sphere as a win indicator.
