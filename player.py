import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter
        self.pos = -1
        self.utility = -9
        
    def get_move(self, game):
        pass
            
        
class HumanPlayer(Player):    
    def letter(self, letter):
        Super().__init__(letter)
    
    def get_move(self, game):
        print('Available boxes: ', end=" ")
        for i in game.available_boxes():
            print(i, end=" ")
        print("\n")
        square = input('Enter choice for player ' + self.letter + ' : ')
        while True:
            if(not square.isdigit()):
                print('Invalid Value, please enter a valid digit')
            else:
                box = int(square)
                if ( 0 > box  or  box > 8 or box not in game.available_boxes()):
                   print('Digit value outside 0 to 8. Please enter again')
                else: 
                    break
            square = input('Enter choice for player ' + self.letter + ' : ')
        return box
        
class ComputerRandomPlayer(Player):    
    def letter(self, letter):
        Super().__init__(letter)
    
    def get_move(self, game):
        random_box = random.randint(0,9)
        while(random_box not in game.available_boxes()):
            random_box = random.randint(0,8)
        
        return random_box
            
class ComputerMinMaxPlayer(Player):        
    def letter(self, letter):
        Super().__init__(letter)
        
    def get_move(self, game):
        pos = ComputerRandomPlayer.get_move(self, game)
        if len(game.available_boxes()) < 8:
            pos = self.min_max_algo(game, self.letter)['position']
        return pos
    
    def min_max_algo(self, game, player): 
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
         
        if game.winner:
            if other_player == max_player:
                return {'position': None, 'score': 1 * (len(game.available_boxes()) + 1)} 
            else:
                return {'position': None, 'score': -1 * (len(game.available_boxes()) + 1)}
        if not game.is_empty: 
            return {'position': None, 'score': 0}       
        
        if (player == max_player):
            best = {'position': None, 'score' : -9}
        else:
            best = {'position': None, 'score' : 9}
            
        for possible_move in game.available_boxes():
            game.mark_box(player, possible_move)
                        
            sim_score = self.min_max_algo(game, other_player)
            
            game.board[possible_move] = "_"
            game.winner = None
            
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
          
        return best