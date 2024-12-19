# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(" | ".join(row)) # Prints each row separated by vertical bars
        print("-" * 9) # Prints a horizontal divider after each row

# Function to check if there's a winner or a draw
def check_winner(board):

    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a draw (no empty spaces left)
    if all(cell != " " for row in board for cell in row):
        return "Draw"
    return None

# Evaluation function to score the board
def evaluate(board):
    winner = check_winner(board)
    if winner == "X":
        return 10
    elif winner == "O":
        return -10
    return 0

# Minimax algorithm to determine the best move
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    # If the game is over, return the score
    if score != 0 or check_winner(board) == "Draw":
        return score - depth if is_maximizing else score + depth

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best_score

# Function to find the best move for the AI
def best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print("You will play as 'O' and the AI will play as 'X'.")
    player = "O"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Winner: {winner}")
            break

        if player == "O":
            try:
                row, col = map(int, input("Enter your move (row and column 0-2, separated by space): ").split())
                if board[row][col] == " ":
                    board[row][col] = "O"
                    player = "X"
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as two numbers between 0 and 2.")
        else:  
            print("AI is making its move...")
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "X"
                player = "O"

# Entry point of the program
if __name__ == "__main__":
    main()
