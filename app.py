# app.py (Flask backend)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [[" "]*3 for _ in range(3)]
current_player = "X"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make_move", methods=["POST"])
def make_move():
    global current_player
    data = request.get_json()
    row, col = data["row"], data["col"]
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner(current_player, board):
            return jsonify({"status": "win", "player": current_player})
        elif check_draw(board):
            return jsonify({"status": "draw"})
        else:
            current_player = "O" if current_player == "X" else "X"
            return jsonify({"status": "success", "player": current_player})
    else:
        return jsonify({"status": "error"})

def check_winner(player, board):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    # Check if any cell is empty
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    # If no cell is empty, the board is full
    return True

if __name__ == "__main__":
    app.run(debug=True)
