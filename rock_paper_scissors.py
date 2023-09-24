import random
import sys

class Scoreboard:
    def __init__(self):
        self.player1_wins = 0
        self.player2_wins = 0
        self.ties = 0
        self.total_wins = {1: 0, 2: 0}  # Track total wins for each player

    def display_score(self):
        if self.player1_wins > 0 or self.player2_wins > 0 or self.ties > 0:
            print('Player 1 Wins: %s, Player 2 Wins: %s, Ties: %s' % (self.player1_wins, self.player2_wins, self.ties))
            print('Total Wins - Player 1: %s, Player 2: %s' % (self.total_wins[1], self.total_wins[2]))

class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number

    def get_move(self):
        while True:
            print(f'{self.name}, enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            move = input()
            if move == 'q':
                sys.exit()
            if move in ('r', 'p', 's'):
                return move
            print('Type one of r, p, s, or q.')

class Game:
    def __init__(self, player1, player2, scoreboard):
        self.player1 = player1
        self.player2 = player2
        self.scoreboard = scoreboard

    def determine_winner(self, move1, move2):
        print(f'Player 1 chose {move1}!')
        print(f'Player 2 chose {move2}!')
        if move1 == move2:
            print('It is a tie!')
            self.scoreboard.ties += 1
        elif (move1 == 'r' and move2 == 's') or \
             (move1 == 'p' and move2 == 'r') or \
             (move1 == 's' and move2 == 'p'):
            print(f'{self.player1.name} wins!')
            self.scoreboard.player1_wins += 1
            self.scoreboard.total_wins[1] += 1
        else:
            print(f'{self.player2.name} wins!')
            self.scoreboard.player2_wins += 1
            self.scoreboard.total_wins[2] += 1

    def play_round(self):
        while True:
            move1 = self.player1.get_move()
            move2 = self.player2.get_move()

            self.determine_winner(move1, move2)
            self.scoreboard.display_score()
            print('Play another round? (y)es or (n)o')
            play_again = input()
            if play_again != 'y':
                break

    def play_game(self):
        print('ROCK, PAPER, SCISSORS')
        while True:
            self.play_round()
            print('Play another game? (y)es or (n)o')
            play_again = input()
            if play_again != 'y':
                break

if __name__ == '__main__':
    player1_name = input('Enter Player 1 name: ')
    player2_name = input('Enter Player 2 name: ')
    player1 = Player(player1_name, 1)
    player2 = Player(player2_name, 2)
    scoreboard = Scoreboard()

    game = Game(player1, player2, scoreboard)
    game.play_game()
