import random

print("Вітаємо! Ви граєте гру хрестики-нулики")
print("Давай розпочнемо 😊")

mode = input("Виберіть режим гри ('simple' для гри з іншим гравцем або 'computer' для гри з комп'ютером): ")

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
first_player = "X"
second_player = "O" if mode == "simple" else "Computer"

game_over = False

while not game_over:
    for row in board:
        print("|".join(row))
        print("_" * 5)

    if first_player == "X" or mode == "simple":
        row = int(input(f"Player {first_player} enter the row (0-2):"))
        col = int(input(f"Player {first_player} enter the col (0-2):"))
    else:
        row, col = random.randint(0, 2), random.randint(0, 2)
        while board[row][col] != " ":
            row, col = random.randint(0, 2), random.randint(0, 2)
        print(f"Computer chose: row {row}, col {col}")

    if board[row][col] == " ":
        board[row][col] = first_player

        winner = False
        for i in range(3):
            if (board[i][0] == first_player and board[i][1] == first_player and board[i][2] == first_player) or \
               (board[0][i] == first_player and board[1][i] == first_player and board[2][i] == first_player):
                winner = True

        if (board[0][0] == first_player and board[1][1] == first_player and board[2][2] == first_player) or \
           (board[0][2] == first_player and board[1][1] == first_player and board[2][0] == first_player):
            winner = True

        if winner:
            for row in board:
                print("|".join(row))
                print("_" * 5)
            print(f"Player {first_player} wins!")
            game_over = True
        else:
            draw = True
            for row in board:
                if " " in row:
                    draw = False
            if draw:
                for row in board:
                    print("|".join(row))
                    print("_" * 5)
                print("It's a draw!")
                game_over = True
            else:
                first_player = "O" if first_player == "X" else "X"
                second_player = "X" if second_player == "O" else "O"
    else:
        print("This spot is already taken. Try again.")

restart = input("Do you want to restart the game? Type 'restart' to play again or 'exit' to quit: ")
if restart == "restart":
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    first_player = "X"
    game_over = False
else:
    game_over = True
    print("Thanks for playing!")

