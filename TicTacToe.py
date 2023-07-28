def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for cell in board[3]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
            return True
    if board[0][2] == board[1][1] == board[2][0] == player:
            return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range[3]]
    players = ["X", "O"]
    current_player = 0
    game_over = False

    while not game_over:
        print_board(board)
        player = players[current_player]
        print("player",player)
        row = int(input["Enter the row (0-2): "])
        col = int(input["Enter the column (0-2): "])

        if board[row][col] == " ":
           board[row][col] = player

           if check_win(board, player):
               print_board(board)
               print("player", player, "wins!")
               game_over = True
            elif all(board[i][j] != " " for i in range[3] for j in range[3]):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = (current_player + 1) % 2
        else:
            print("Invalid move. Try again.")
    
    play_game()
