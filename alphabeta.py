# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function for Depth-First Search to simulate the game with Alpha-Beta Pruning
def dfs(board, player, alpha, beta, depth=0):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif is_board_full(board):
        return 0

    if player == 'X':
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = dfs(board, 'O', alpha, beta, depth + 1)
                    board[i][j] = ' '
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return max_score
    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = dfs(board, 'X', alpha, beta, depth + 1)
                    board[i][j] = ' '
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return min_score

# Function to find the best move using DFS with Alpha-Beta Pruning
def find_best_move(board):
    alpha = float('-inf')
    beta = float('inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = dfs(board, 'O', alpha, beta)
                board[i][j] = ' '
                if score > alpha:
                    alpha = score
                    best_move = (i, j)
        
    return best_move

# Function to play the Tic Tac Toe game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        if current_player == 'X':
            row, col = find_best_move(board)
            board[row][col] = 'X'
        else:
            while True:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    break
                else:
                    print("Invalid move. Try again.")
            board[row][col] = 'O'

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

# Start the game
play_game()
