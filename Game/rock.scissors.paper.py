#rock , paper , scissors
#lower() : horof bozorg va kochik eror nemide
#with for : for time in range(0,3)
import random
print('rock')
print('paper')
print('scissors')

randomNumber = random.randint(0,2)
computerMove = 'rock'
if randomNumber == 0:
    computerMove = 'rock'
elif randomNumber == 1:
    computerMove = 'paper'
elif randomNumber == 2:
    computerMove = 'scissors'

player1_win = 0
player2_win = 0
winningScore = 4

while player1_win < winningScore and player2_win < winningScore:
    print(f'player1 : {player1_win} and player2 : {player2_win}')
    player_1 = input('player_1 makw your move :').lower()
    player_2 = computerMove
    print(f'player_2 make your move : {computerMove}')

    if player_1 == 'quit': # khoroj az bazi heyn ejra
        break

    if player_1 == player_2 :
            print('this is a tie')
    elif player_1 == 'rock':
        if player_2 == 'paper':
            print('player_2 wins')
            player2_win += 1      # player2_wins +1 baraye jologiri az bi nahayat ejra
        elif player_2 == 'scissors':
            print('player_1 wins')
            player1_win += 1
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('player_1 wins')
            player1_win += 1
        elif player_2 == 'scissors':
            print('player_2 wins')
            player2_win += 1
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print('player_2 wins')
            player2_win += 1
        elif player_2 == 'paper':
            print('player_1 wins')
            player1_win += 1
    else:
        print('somthing went wrong')
