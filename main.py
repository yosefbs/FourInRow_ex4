from Board import Board, Color
from GameEngine import GameEngine
from player import *

if __name__ == '__main__':
    # b = Board()
    # p1 = MachineLogicPlayer(b, Color.RED)
    # p2 = HumanPlayer(Color.YELLOW)
    # eng = GameEngine()
    # eng.play_game(b, p1, p2,True)
    # b.print_board()


    r_wins=0
    y_wins=0
    num_of_play=1000
    for i in range(1000):
        b = Board()
        p1 = MachineLogicPlayer(b,Color.RED)
        p2 = MachineRandomPlayer(Color.YELLOW)
        eng = GameEngine()
        eng.play_game(b,p1,p2)
        b.print_board()
        if b.winner == Color.YELLOW:
            y_wins+=1
        else:
            r_wins+=1
        print('================================')
    print('red wins: {0} total games: {1} ratio: {2}'.format(r_wins,num_of_play,r_wins/num_of_play))
    print()

