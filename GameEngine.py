

class GameEngine:
    WORKER_POOL = None
    def play_game(self,board,player1,player2,print_moves=False,print_winner=True):
        win = False
        while True:
            selectedCol = player1.play(board.available_columns())
            win = board.add_to_col(selectedCol,player1.color)
            if win:
                break
            if print_moves:
                board.print_board()
                print()
            selectedCol = player2.play(board.available_columns())
            win = board.add_to_col(int(selectedCol), player2.color)
            if win or len(board.available_columns())==0:
                break
            if print_moves:
                board.print_board()
                print()
        if print_winner:
            print('The winner is: {0} - '.format(board.winner) ,end='')
            print(board.winner)
        return board.winner


