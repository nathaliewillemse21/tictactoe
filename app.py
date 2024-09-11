# Tic-Tac-Toe game in Python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# Define the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--|---|--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--|---|--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

# Function to check if a player has won
def check_winner(player):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to handle player moves
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = player
                break
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

# Main game loop
def play_game():
    current_player = 'X'
    
    while True:
        print_board()
        player_move(current_player)

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
