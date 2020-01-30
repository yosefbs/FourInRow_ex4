import datetime
import multiprocessing
import operator

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
    print()
    print('============ {0} start ================'.format(run_name))
    print("Player 1 (RED) = Heuristic VS Player 2 (Yellow) MonteCarlo")
    for i in range(num_of_play):
        b = Board()
        p1 = MachineLogicPlayer(b, Color.RED)
        p2 = MonteCarloPlayer(b, Color.YELLOW)
        # p2 = MachineRandomPlayer(Color.YELLOW)
        eng = GameEngine()
        eng.play_game(b, p1, p2, False, False)
        # b.print_board()
        if b.winner == Color.YELLOW:
            y_wins += 1
        elif b.winner == Color.RED:
            r_wins += 1
        print(str(i + 1) + " " + str(b.winner) + " wins - " + str(datetime.datetime.now().time()))
        # print('red wins: {0} yellow wins: {1} games: {2}'.format(r_wins, y_wins, i + 1))

    print('============ {0} complete ================'.format(run_name))
    print('red wins: {0} total games: {1} ratio: {2}'.format(r_wins, num_of_play, r_wins / num_of_play))
    return r_wins


# function for tuning heuristic player(Ex_2)
# the function change the reward for some state and check the impact of wining statistic
def tuneLogicalPlayer():
    # wins = {}
    run_games = 10
    hill_climbing_runs = 1000
    MonteCarloPlayer.N = 300
    MachineLogicPlayer.twoInRowReward = 0
    max_wins = 0
    prev_step_wins = 0
    reward_change_diff = 4
    direct = [operator.add, operator.sub]  # hill claiming direct up(add) or down(sub)
    cur_direct_index = 0
    for i in range(hill_climbing_runs):
        wins = runMultiGames(run_games, 'reward = {0}'.format(MachineLogicPlayer.twoInRowReward))
        print(printFormat.format(i, wins, run_games, wins / run_games))
        if wins > max_wins:
            max_wins = wins

        if wins < prev_step_wins:
            reward_change_diff = reward_change_diff / 2
            cur_direct_index = (cur_direct_index + 1) % 2
        MachineLogicPlayer.twoInRowReward =direct[cur_direct_index](MachineLogicPlayer.twoInRowReward,reward_change_diff)
        prev_step_wins = wins

    # for i in range(2, 8):
    #     MachineLogicPlayer.twoInRowReward = i
    #     wins[i] = runMultiGames(run_games, 'reward = {0}'.format(i))
    # for i in range(2, 8):
    #     print(printFormat.format(i, wins[i], run_games, wins[i] / run_games))


printFormat = 'when reward for 2 in a row is: {0} red wins: {1} total games: {2} ratio: {3}'

if __name__ == '__main__':
    GameEngine.WORKER_POOL = multiprocessing.Pool(processes=4)
    # uncomment next lines for human vs machine game

    # b = Board()
    # p1 = MachineLogicPlayer(b, Color.RED)
    # # p1 = MachineRandomPlayer(Color.RED)
    # # p1 = HumanPlayer(Color.RED)
    # # p2 = HumanPlayer(Color.YELLOW)
    # # p2 = MachineLogicPlayer(b, Color.YELLOW)
    # p2 = MonteCarloPlayer(b,Color.YELLOW)
    # eng = GameEngine()
    # eng.play_game(b, p1, p2,True)
    # b.print_board()

    tuneLogicalPlayer()
