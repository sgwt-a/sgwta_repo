import random


# ボードの初期化
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


# ボードの表示
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


# 空いているマスを取得
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]


# 勝者判定
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


# ゲーム終了判定
def is_game_over(board):
    return check_winner(board) is not None or not get_available_moves(board)


# ミニマックス法の実装
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":  # CPUが勝ち
        return 10 - depth
    if winner == "X":  # プレイヤーが勝ち
        return depth - 10
    if not get_available_moves(board):  # 引き分け
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for r, c in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(best_score, score)
        return best_score


# CPUの最適な手を決定
def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for r, c in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move


# メインゲームループ
def play_game():
    board = initialize_board()
    print("Tic-Tac-Toe: You are X, CPU is O")

    player_turn = random.choice([True, False])  # 先攻をランダム決定
    print("You go first!" if player_turn else "CPU goes first!")

    while not is_game_over(board):
        print_board(board)
        if player_turn:
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    r, c = divmod(move, 3)
                    if board[r][c] == " ":
                        board[r][c] = "X"
                        break
                    else:
                        print("Invalid move. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter a number from 1 to 9.")
        else:
            print("CPU is thinking...")
            move = get_best_move(board)
            if move:
                r, c = move
                board[r][c] = "O"

        player_turn = not player_turn  # ターン交代

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()
