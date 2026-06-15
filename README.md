# AI Assignment Project

This project demonstrates three fundamental Artificial Intelligence concepts through practical Python implementations:

* **Alpha-Beta Pruning** with game tree visualization
* **Hidden Markov Model (HMM)** decoding using the Viterbi algorithm
* **Tic-Tac-Toe AI** using the Minimax algorithm with Alpha-Beta pruning

The project focuses on search algorithms, probabilistic reasoning, and adversarial game playing.

---

## Project Overview

### 1. Alpha-Beta Pruning (`alpha_beta_prunning.py`)

An implementation of the Alpha-Beta Pruning algorithm for optimizing Minimax search in game trees.

#### Features

* Constructs a game tree structure
* Performs Minimax search with Alpha-Beta pruning
* Visualizes explored and pruned branches using Graphviz
* Tracks Alpha and Beta values during traversal
* Generates graphical output of the search process

#### Output

* `alpha_beta_tree.gv.png` — visualization of the game tree

---

### 2. Hidden Markov Model - Viterbi Algorithm (`hmm.py`)

An implementation of the Viterbi algorithm for finding the most probable sequence of hidden states in a Hidden Markov Model.

#### Features

* Solves the HMM decoding problem
* Supports custom transition and emission probabilities
* Computes the optimal hidden state sequence
* Visualizes state probabilities using Matplotlib
* Displays probability trends over time

#### Output

* Terminal output showing the predicted hidden state sequence
* `viterbi_hmm.png` — probability visualization

---

### 3. Tic-Tac-Toe with AI (`tic_tac_toe.py`)

An interactive command-line Tic-Tac-Toe game against an AI opponent.

#### Features

* Human vs AI gameplay
* AI uses Minimax with Alpha-Beta pruning
* Interactive terminal interface
* Automatic win and draw detection
* Optimal AI strategy that never loses

---

## Project Structure

```text
College Work/
├── README.md
├── requirements.txt
├── alpha_beta_prunning.py
├── hmm.py
├── tic_tac_toe.py
├── alpha_beta_tree.gv.png
└── viterbi_hmm.png
```

---

## Requirements

* Python 3.6 or higher
* Graphviz (system package)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd "College Work"
```

Or extract the ZIP file and open the project directory.

---

### Step 2: Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Graphviz

Graphviz must be installed separately because the Python package only provides bindings.

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install graphviz
```

#### Fedora

```bash
sudo dnf install graphviz
```

#### Arch Linux / Manjaro

```bash
sudo pacman -S graphviz
```

#### Verify Installation

```bash
dot -V
```

Expected output:

```text
dot - graphviz version X.X.X
```

---

### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Dependencies

The project uses the following Python libraries:

* `numpy`
* `matplotlib`
* `graphviz`
* `Pillow`
* `contourpy`
* `cycler`
* `kiwisolver`
* `packaging`
* `pyparsing`
* `python-dateutil`

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Alpha-Beta Pruning

```bash
python3 alpha_beta_prunning.py
```

#### Output

* Displays evaluation results in the terminal
* Generates a game tree visualization
* Creates:

```text
alpha_beta_tree.gv.png
```

---

### Hidden Markov Model - Viterbi Algorithm

```bash
python3 hmm.py
```

#### Output

* Prints the most likely hidden state sequence
* Displays probability calculations
* Generates:

```text
viterbi_hmm.png
```

---

### Tic-Tac-Toe AI

```bash
python3 tic_tac_toe.py
```

#### How to Play

* The AI plays as `X`
* The player plays as `O`
* Enter row and column values when prompted

Example board:

```text
    0   1   2
  +---+---+---+
0 |   |   |   |
  +---+---+---+
1 |   |   |   |
  +---+---+---+
2 |   |   |   |
  +---+---+---+
```

Example input:

```text
Enter row: 1
Enter column: 1
```

The game ends when either player wins or the board is full.

---

## Algorithm Complexity

| Algorithm               | Time Complexity                         | Space Complexity |
| ----------------------- | --------------------------------------- | ---------------- |
| Alpha-Beta Pruning      | O(b^(d/2)) best case, O(b^d) worst case | O(d)             |
| Viterbi Algorithm       | O(N² × T)                               | O(N × T)         |
| Minimax with Alpha-Beta | O(b^(d/2)) best case                    | O(d)             |

Where:

* `b` = branching factor
* `d` = search depth
* `N` = number of hidden states
* `T` = observation sequence length

---

## Applications

### Alpha-Beta Pruning

* Chess engines
* Board game AI
* Decision-making systems

### Hidden Markov Models

* Speech recognition
* Natural language processing
* DNA sequence analysis
* Activity recognition

### Minimax Algorithm

* Turn-based games
* Strategic planning
* Competitive AI systems

---

## Troubleshooting

### `ModuleNotFoundError`

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

### `graphviz.backend.execute.ExecutableNotFound`

Graphviz is not installed or is not available in your system PATH.

Verify installation:

```bash
dot -V
```

If the command fails, install Graphviz using your distribution's package manager.

---

### Visualization Files Are Not Generated

Ensure Graphviz is correctly installed:

```bash
which dot
```

Expected output:

```text
/usr/bin/dot
```

---

### Permission Denied Error

Make sure Python scripts have execution permission:

```bash
chmod +x *.py
```

---

## Notes

* The project has been tested on Linux environments.
* A virtual environment is strongly recommended.
* Generated image files are overwritten each time the scripts are executed.

---

## Author

Developed as part of an Artificial Intelligence coursework assignment.
