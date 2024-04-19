import tkinter as tk
from tkinter import messagebox

def play_move(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(current_player):
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            player_label.config(text=f"Player {current_player}'s turn")

def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    # Check if the board is full
    return all(cell != " " for row in board for cell in row)

def reset_game():
    global board, current_player
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")
    player_label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

board = [[" "]*3 for _ in range(3)]
current_player = "X"

buttons = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: play_move(row, col))
        buttons[i][j].grid(row=i, column=j)

player_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 14))
player_label.grid(row=3, columnspan=3)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, columnspan=3)

root.mainloop()
