import random
from  colorama import Fore, Back, Style, init

init(autoreset = False)
print("Вітаємо! Ви граєте гру хрестики-нулики")
print("Давай розпочнемо 😊")
mode = input("Виберіть режим гри. Для того щоб вибрати, необхідно вписати команду 'simple' або 'computer' для гри з комп'ютером: ")
# pole = int(input("Виберіть "))
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
first_player = "X"
x_wins = 0
o_wins = 0
draws = 0


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
            row, col = random.randint(0,2), random.randint(0,2)
    print(f"Computer chose: row {row}, col {col}")
            
    if board[row][col] == " ":
        board[row][col] = first_player

        winner = False
        for i in range(3):
            if (board[i][0] == first_player and board[i][1] == first_player and board[i][2] == first_player) or (board[0][i] == first_player and board[1][i] == first_player and board[2][i] == first_player):
              winner = True

        if (board[0][0] == first_player and board[1][1] == first_player and board[2][2] == first_player) or (board[0][2] == first_player and board[1][1] == first_player and board[2][0] == first_player):
            winner = True

        if winner: 
            for row in board: 
                print("|".join(row)) 
                print("_" * 5) 

            print(f"Player {first_player} wins!") 
            game_over = True
            if first_player == "X":
                x_wins += 1
            else:
                o_wins += 1
        
            restart = input("Ти хочеш перезапустити гру? Тоді треба ввести команду 'restart' щоб грати знову або 'exit' щоб вийти: ")
            if restart == "restart":
                board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                first_player = "X"
                game_over = False
            else:
                game_over = True
                print("Дякую за гру!")

        else:
            draw = True
            for row in board:
                if " " in row:  # Якщо є порожня клітинка, нічиї немає
                    draw = False
                    break

            if draw:
                for row in board:
                    print("|".join(row))
                    print("_" * 5)
                print("It's a draw!")
                game_over = True
                draws += 1

            else:
                first_player = "O" if first_player == "X" else "X"
  
    else: 
      print("This spot is already taken. Try again.")

print(f"Player X wins: {x_wins}, player O wins: {o_wins} , draws: {draws} ")