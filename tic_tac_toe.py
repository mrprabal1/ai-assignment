import math
import os
 
AI    = 'X'
HUMAN = 'O'
EMPTY = '.'
 
def print_board(board):
    print()
    print("    0   1   2")
    print("  +-----------+")
    for r, row in enumerate(board):
        cells = []
        for cell in row:
            cells.append(f" {cell} ")
        print(f"{r} |{'|'.join(cells)}|")
        if r < 2:
            print("  +---+---+---+")
    print("  +-----------+")
    print()
 
def moves_left(board):
    return any(board[r][c] == EMPTY for r in range(3) for c in range(3))
 
def evaluate(board):
    lines = (
        [(r, 0), (r, 1), (r, 2)] for r in range(3)
    )
    lines = list(lines) + [
        [(0, c), (1, c), (2, c)] for c in range(3)
    ] + [
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]
    for line in lines:
        vals = [board[r][c] for r, c in line]
        if vals == [AI]*3:    return 10
        if vals == [HUMAN]*3: return -10
    return 0
 
def minimax(board, depth, is_max, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)
    if score ==  10: return score - depth
    if score == -10: return score + depth
    if not moves_left(board): return 0
 
    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = AI
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[r][c] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return best
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[r][c] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha:
                        return best
        return best
 
def best_move(board):
    top_val, top_pos = -math.inf, (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = AI
                val = minimax(board, 0, False)
                board[r][c] = EMPTY
                if val > top_val:
                    top_val, top_pos = val, (r, c)
    return top_pos
 
def check_end(board):
    score = evaluate(board)
    if score == 10:
        print_board(board)
        print("  >> AI wins! Better luck next time.")
        return True
    if score == -10:
        print_board(board)
        print("  >> You win! Somehow.")
        return True
    if not moves_left(board):
        print_board(board)
        print("  >> It's a draw!")
        return True
    return False
 
def human_turn(board):
    while True:
        try:
            row = int(input("  Row    (0/1/2): "))
            col = int(input("  Column (0/1/2): "))
        except ValueError:
            print("  Please enter a number.\n")
            continue
 
        if row not in range(3) or col not in range(3):
            print("  Out of bounds. Try again.\n")
        elif board[row][col] != EMPTY:
            print("  Cell already taken. Try again.\n")
        else:
            board[row][col] = HUMAN
            break
 
def main():
    board = [[EMPTY]*3 for _ in range(3)]
 
    print()
    print("  ================================")
    print("   Tic-Tac-Toe  |  Human(O) vs AI(X)")
    print("  ================================")
    print("  You go first. Enter row and column (0-2).")
    print("  Empty cells shown as '.'")
    print_board(board)
 
    while True:
        print("  --- Your move ---")
        human_turn(board)
        if check_end(board): break
 
        print("  AI is thinking...")
        r, c = best_move(board)
        board[r][c] = AI
        print(f"  AI plays -> row {r}, col {c}\n")
        if check_end(board): break
 
        print_board(board)
 
if __name__ == "__main__":
    main()
