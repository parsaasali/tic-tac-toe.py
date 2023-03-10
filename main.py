from functions import drawing, winner

player1 = input('player one, enter your name : ')
player2 = input('player two, enter your name : ')
print(f"hello,\twelcome to Tic-Tac-Toe.\nplayers {player1.title()} and {player2.title()} are competing to earn the first stage ")
print('X goes first, then O')
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # '4' ==> 'X'  3 ==> 'X'
player1_move_list = []
player2_move_list = []
slotsfilled = 0
counter = 1
winstatment_1 = board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]
winstatment_2 = board[0] == board[4] == board[8] or board[2] == board[4] == board[6]
    
drawing(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])

while slotsfilled < 9:
    
    player1_move = input(f'{player1.title()}, enter your {counter}. move : ')
    while player1_move in player2_move_list or player1_move in player1_move_list:
        print('enter a valid place')
        player1_move = input(f'{player1.title()}, enter your {counter}. move : ')
    
    board[int(player1_move)-1] = 'X'
    player1_move_list.append(player1_move)
    slotsfilled += 1
    
    drawing(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
    winner(winstatment_1=winstatment_1, winstatment_2=winstatment_2, player=player1)
    
    player2_move = input(f'{player2.title()}, enter your {counter}. move : ')
    while player2_move in player2_move_list or player2_move in player1_move_list:
        print('enter a valid place')
        player2_move = input(f'{player1.title()}, enter your {counter}. move : ')
        
    board[int(player2_move)-1] = 'O'
    player2_move_list.append(player2_move)
    slotsfilled += 1
    
    drawing(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
    winner(winstatment_1=winstatment_1, winstatment_2=winstatment_2, player=player2)
    
    counter += 1
    
if slotsfilled == 8:
    print('no one wins!')