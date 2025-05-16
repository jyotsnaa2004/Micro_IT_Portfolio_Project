import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("300x330")
window.resizable(False, False)
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False
def check_draw():
    for row in board:
        if "" in row:
            return False
    return True
def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            disable_all_buttons()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_all_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["state"] = "disable"
def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda r=i, c=j: button_click(r, c))
        buttons[i][j].grid(row=i, column=j)
reset_btn = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_game)
reset_btn.place(x=110, y=290)
window.mainloop()