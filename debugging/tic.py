def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Input out of range! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
