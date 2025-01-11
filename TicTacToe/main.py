from tic_tac_toe import TicTacToeGame

def main():
    game = TicTacToeGame()
    winner = game.start_game()
    print("winner is: ", winner)
    # if winner != "It's a tie":
    #     print("Yay, " + winner + " won the match!")
    # else:
    #     print("It's a tie")


if __name__ == "__main__":
    main()
