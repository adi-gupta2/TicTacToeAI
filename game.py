from player import HumanPlayer, ComputerRandomPlayer, ComputerMinMaxPlayer
import time

class Game():
    def __init__(self):
        self.board = ['_' for _ in range(9)]
        self.winner = None
        
    def mark_box(self, player, position):   
        self.board[position] = player
        if Game.winner(self, player, position):
            self.winner = player
        
    
    def winner(self, player, position):
        vertical = position % 3 
        horizontal = int(position / 3)
        diag1 = [2,4,6]
        diag2 = [0,4,8]
        if all(player == self.board[i * 3 + vertical] for i in range(3)): #vertical
            return True
        if all(player == self.board[horizontal * 3 + i] for i in range(3)): #horizontal 
            return True
        if all(player == self.board[i] for i in diag1): #first diagonal
            return True
        if all(player == self.board[i] for i in diag2): #second diagonal
            return True
        return False
                
    def available_boxes(self):
        return [i for i in range(9) if self.board[i] == "_" ]
       
    def declare_winner(self):
        print('Congratulation player ' + self.winner + ' !! You have won.')
      
    def print_board(self):
        for i in range(3):
            print("| ", end = "")
            for j in range(3):                
                print(self.board[i * 3  + j], end=" | " )
            print("\n")
            
    def print_starting_board(self):
        for i in range(3):
            print("| ", end = "")
            for j in range(3):                
                print(i * 3  + j, end=" | " )
            print("\n")
            
    def is_empty(self):
        return True if any(i == "_" for i in self.board) else False      
            
def play(game, o_player, x_player):
    next_player = 'O'
    while (not game.winner and game.is_empty()):
        if (next_player == 'O'):
            position =  o_player.get_move(game)
        else:
            position = x_player.get_move(game)
        print(next_player + "'s chance: \n")
        game.mark_box(next_player, position)
        game.print_board()
        if next_player == 'O':
            next_player = 'X'
        else:
            next_player = 'O'
        # time.sleep(1)
        
    if (game.winner):
        game.declare_winner()
    else:
        print('It\'s a tie.')
            

if __name__ == '__main__':
    new_game = Game()
    o_player = HumanPlayer('O')
    x_player = ComputerMinMaxPlayer('X')
    new_game.print_starting_board()
    play(new_game, o_player, x_player)