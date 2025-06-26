import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for winner or draw
def check_winner(board):
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

# Minimax Algorithm
def minimax(board, is_maximizing):
    result = check_winner(board)
    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best = min(score, best)
        return best

# Get the best move for AI
def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to play the game
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!\nYou are X, AI is O.")
    print_board(board)

    while True:
        # Player Move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already taken.")
            except:
                print("Invalid input. Try again.")

        print_board(board)
        result = check_winner(board)
        if result:
            print(f"Result: {result} wins!" if result != "Draw" else "It's a draw!")
            break

        # AI Move
        ai_r, ai_c = best_move(board)
        board[ai_r][ai_c] = "O"
        print("AI played:")
        print_board(board)
        result = check_winner(board)
        if result:
            print(f"Result: {result} wins!" if result != "Draw" else "It's a draw!")
            break

play()
