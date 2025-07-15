import random
board = [1,2,3,4,5,6,7,8,9]

def display_board(board):
     print('+---+---+---+')
     print(f'| {board[0]} | {board[1]} | {board[2]} |')
     print('+---+---+---+')
     print(f'| {board[3]} | {board[4]} | {board[5]} |')
     print('+---+---+---+')
     print(f'| {board[6]} | {board[7]} | {board[8]} |')
     print('+---+---+---+')

def user_move(board):
     while True:
          move = input('Enter a number from (1-9):')
          #if move in range (1,10):
           #    continue
          #else:
           #    print('Enter a valid number:')
          if not move.isdigit():
               print("Please enter a number:")
               continue
          move = int(move)
          if move < 1 or move > 9:
               print('Chose a number between 1 to 9:')
               continue
          if board[move-1] in ['X', 'O']:
               print('The cell is already taken please select another one:')
               continue
          board[move-1] = 'O'
          break

def computer_move(board):
     empty_cells = [i for i in range(9) if board[i] not in ['X', 'O']]
     if empty_cells:
         move = random.choice(empty_cells)
         board[move] = 'X'
         print(f"computer choose position{move + 1}")

def check_winner(board, player):
      wins = [
        [0, 1, 2], 
        [3, 4, 5],  
        [6, 7, 8],  
        [0, 3, 6],  
        [1, 4, 7],  
        [2, 5, 8],  
        [0, 4, 8],  
        [2, 4, 6]
      ]
      for combo in wins:
           if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
      return False     
def check_tie(board):
    return all (cell in ["X", "O"] for cell in board)
board[4] ='X'

while True:
 display_board(board)
 user_move(board)
 if check_winner(board, 'O'):
        display_board(board)
        print('You Win')
        break
 if check_tie(board):
        display_board(board)
        print('Its a tie')
        break
  
 computer_move(board)
 if check_winner(board, 'X'):
        display_board(board)
        print('Computer Win')
        break
 if check_tie(board):
        display_board(board)
        print('Its a tie')
        break