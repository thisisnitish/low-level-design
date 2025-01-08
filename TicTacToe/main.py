from tic_tac_toe import TicTacToeGame

def main():
    game = TicTacToeGame()
    winner = game.start_game()
    print("Yay, " + winner + " won the match!")


if __name__ == "__main__":
    main()
