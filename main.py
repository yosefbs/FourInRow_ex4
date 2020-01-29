import datetime
import multiprocessing

from player import *
from Board import Board, Color
from GameEngine import GameEngine


# function to run multiple games in a row
# input: num_of_play = num of required play
#        run_name = logical name of run for print only
# the function run <num of play> games and print the win statistic
def runMultiGames(num_of_play, run_name=""):
    r_wins = 0
    y_wins = 0
    print('============ {0} start ================'.format(run_name))
    for i in range(num_of_play):
        print(str(i + 1) + "-" + str(datetime.datetime.now().time()))
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
        # print('red wins: {0} yellow wins: {1} games: {2}'.format(r_wins, y_wins, i + 1))
        print('============================')
    print('============ {0} complete ================'.format(run_name))
    print('red wins: {0} total games: {1} ratio: {2}'.format(r_wins, num_of_play, r_wins / num_of_play))
    return r_wins


# function for tuning heuristic player(Ex_2)
# the function change the reward for some state and check the impact of wining statistic
def tuneLogicalPlayer():
    wins = {}
    run_games = 10
    for i in range(2, 8):
        MachineLogicPlayer.twoInRowReward = i
        wins[i] = runMultiGames(run_games, 'reward = {0}'.format(i))
    for i in range(2, 8):
        print('when reward for 2 in a row is: {0} red wins: {1} total games: {2} ratio: {3}'.format(i,wins[i], run_games, wins[i] / run_games))


if __name__ == '__main__':
    GameEngine.WORKER_POOL = multiprocessing.Pool(processes=4)
    # uncomment next lines for human vs machine game

    # b = Board()
    # # p1 = MachineLogicPlayer(b, Color.RED)
    # # p1 = MachineRandomPlayer(Color.RED)
    # p1 = HumanPlayer(Color.RED)
    # # p2 = HumanPlayer(Color.YELLOW)
    # # p2 = MachineLogicPlayer(b, Color.YELLOW)
    # p2 = MonteCarloPlayer(b,Color.YELLOW)
    # eng = GameEngine()
    # eng.play_game(b, p1, p2,True)
    # b.print_board()

    tuneLogicalPlayer()
