# Initialize the board
import math


board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move, try again.")
        player_move()

def game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'O'
        print_board()
        if is_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    game()