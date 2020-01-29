import datetime

from Board import Board, Color
from GameEngine import GameEngine

if __name__ == '__main__':
    from player import *

    # b = Board()
    # # p1 = MachineLogicPlayer(b, Color.RED)
    # p1 = MachineRandomPlayer(Color.RED)
    # # p1 = HumanPlayer(Color.RED)
    # # p2 = HumanPlayer(Color.YELLOW)
    # p2 = MonteCarloPlayer(b,Color.YELLOW)
    # eng = GameEngine()
    # eng.play_game(b, p1, p2,True)
    # b.print_board()

    #
    r_wins = 0
    y_wins = 0
    num_of_play = 15
    for i in range(num_of_play):
        print(str(i) + "-" + str(datetime.datetime.now().time()))
        b = Board()
        p1 = MachineLogicPlayer(b, Color.RED)
        p2 = MonteCarloPlayer(b, Color.YELLOW)
        # p2 = MachineRandomPlayer(Color.YELLOW)
        eng = GameEngine()
        eng.play_game(b, p1, p2)
        b.print_board()
        if b.winner == Color.YELLOW:
            y_wins += 1
        elif b.winner == Color.RED:
            r_wins += 1
        print('red wins: {0} yellow wins: {0} total games: {2}'.format(r_wins, y_wins, num_of_play))
        print('================================')
    print('red wins: {0} total games: {1} ratio: {2}'.format(r_wins, num_of_play, r_wins / num_of_play))
    print()
