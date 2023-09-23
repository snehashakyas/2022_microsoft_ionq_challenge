# Quantum Tetris

Developed for MIT IQUHACK 2022 
Group name: Quantris
Group members: `Caspian Chaharom, Danai Bili, Frederik Hardervig, Sneha Shakya, Tomasz Kazulak`

For the MIT iQuHACK Hackathon, the team's task was a 26 hour Microsoft and IonQ joint challenge to use a quantum computer to build a game. Thus the team developed this Quantum Tetris game that introduces quantum concepts, such as destructive interference, through a familiar-inspired game of Tetris.

Awardees of the "Creativity Hack Award" for MIT IQUHACK 2022, 

## Game Rules and Goal

Quantim Tetris is designed to teach quantum concepts in a fun and interactive manner. It is inspired by the familiar game of Tetris. 

In this game, your Tetris blocks are Qubits, and you must make them destructively interfere to get rid of them. 

There are two types of blocks:
* Single qubit blocks:
  * The arrows represent the quantum state of the qubit. The `|0>` basis is the x-axis and the `|1>` basis vector is the y-axis. So a Hadamard gate applied to `|0>` would make `1/√2 (|0>+|1>)` which would be an arrow pointing in the up-right direction 
  * You can apply the pauli `x` and `z` gates and Hadamard `h` gate by clicking the buttons or pressing the keys on the keyboard
  * The goal of the game is to have the blocks disappear using destructive interference
* Two qubit blocks:
  * Some blocks have two qubits. The single qubit gates operate on the first qubit
  * There are also two two-qubit gates, the controlled x `CX` and controlled z `CZ`, which you can apply by clicking the buttons on the screen, or pressing the keys `a` and `s`, which are directly above their single qubit counterparts on the keyboard

## How to run

Run `python Amalgamation.py` after installing the dependencies `numpy` and `pygame`

## GitHub Repo: https://github.com/CaspianChaharom/Quantum-Tetris


## Pictures
Mapping to qubit states to arrow direction:
![](Pictures/Clock.png)
Screenshot of game during play
![](Pictures/Game.png)


## MIT IQUHACK 2022: Our team's experience

After a hectic couple of days of meetings and lots of hacking, we will remember MIT IQUHACK 2022 for the invaluable experience of getting to run Quantum simulations, but also the fantastic opportunity of getting to know so many passionate hackers and scientists. Overall, despite this being the first hackathon for some of us, we were still able to envision, create (and debug) a full project from scratch, which served as an incredible introduction into the field. Of course, this wouldn't have been possible without the tremendous support of the whole community! 
