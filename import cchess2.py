import chess

# Initialize the board
board = chess.Board()

# Game loop
while not board.is_game_over():
    print(board)
    print("\n")
    
    # Get move from user
    move = input("Enter move (e.g., e2e4): ")
    
    try:
        # Push legal move
        board.push_san(move)
    except ValueError:
        print("Illegal move, try again.")

print("Game Over")
print("Result: " + board.result())
