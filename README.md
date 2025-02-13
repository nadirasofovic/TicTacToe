# Tic Tac Toe with Minimax Algorithm

This project is an implementation of the **Tic Tac Toe** game with an AI player powered by the **Minimax algorithm**. The AI is designed to play optimally against a human player, making the game challenging and fun.

The Minimax algorithm is widely used in game theory and artificial intelligence (AI) for decision-making in two-player games like Tic Tac Toe. It aims to find the best possible move for the AI by simulating all possible moves and counter-moves and evaluating each state of the game.

## How It Works

### Minimax Algorithm Overview

The **Minimax algorithm** is based on creating a decision tree where:
- **Maximizing player (AI)** tries to maximize its score.
- **Minimizing player (human)** tries to minimize the AI's score.

Each terminal state of the game is evaluated as follows:
- **+10** for AI win (Maximizing player).
- **-10** for Human win (Minimizing player).
- **0** for a draw.

The AI uses the algorithm to explore all possible future moves, recursively evaluating the best outcome for itself by simulating the human's possible responses. The AI will always try to get the highest possible score, while the human player tries to minimize the AI's score.
