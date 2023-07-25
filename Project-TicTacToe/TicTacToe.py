"""
Explanation:

print_board(board): This function is used to print the Tic Tac Toe board. It takes the current state of the board as input and prints it in a user-friendly format.

check_win(board, player): This function checks if a given player has won the game. It checks for three-in-a-row matches in rows, columns, and diagonals. If the player has three matching symbols in a row, the function returns True; otherwise, it returns False.

is_board_full(board): This function checks if the board is full, meaning no more moves are possible. It returns True if all the cells on the board are filled, otherwise False.

tic_tac_toe(): This is the main function that implements the Tic Tac Toe game logic. It initializes the empty board, defines the players ("X" and "O"), and uses a while loop to keep the game running until the board is full or a player wins. It takes player input for row and column and validates the move before updating the board. After each move, it checks for a win using check_win and alternates the players to take their turns.

__name__ == "__main__": This line ensures that the tic_tac_toe() function is only called when the script is executed directly, not when it's imported as a module in another script.
"""

def print_board(board):
	for row in board:
		print("|".join(row))
		print("-"*5)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = 0

    while not is_board_full(board):
        print_board(board)
        current_player = players[player_idx]
        print(f"Player {current_player}'s turn.")
        
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                break
            print("Invalid move. Try again.")

        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        player_idx = (player_idx + 1) % 2

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
