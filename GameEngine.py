

class GameEngine:
    WORKER_POOL = None
    def play_game(self,board,player1,player2,print_moves=False,print_winner=True):
        win = False
        while True:
            if len(board.available_columns()) == 0:
                break
            selectedCol = player1.play(board.available_columns())
            win = board.add_to_col(selectedCol,player1.color)
            available_col = board.available_columns()
            if win or len(available_col)==0:
                break
            if print_moves:
                board.print_board()
                print()
            selectedCol = player2.play(available_col)
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


