from typing import List

from models.player import Player
from models.board import Board
from models.playing_piece_X import PlayingPieceX
from models.playing_piece_O import PlayingPieceO
from models.piece_type import PieceType

class TicTacToeGame:
    players: List[Player] = []
    board: Board = None

    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        cross = PlayingPieceX()
        zero = PlayingPieceO()

        p1 = input("Name the Player 1: ")
        p2 = input("Name the Player 2: ")

        p1_sign = input("What piece Player 1 want to choose, X or O ? ")
        p2_sign = input("What piece Player 2 want to choose, X or O ? ")

        if p1_sign == p2_sign:
            raise ValueError("Player 1 and Player 2 can't have same piece")
        
        if p1_sign.upper() == 'X':
            player1 = Player(p1, cross)
            self.players.append(player1)
        else:
            player1 = Player(p1, zero)
            self.players.append(player1)

        if p2_sign.upper() == 'X':
            player2 = Player(p2, cross)
            self.players.append(player2)
        else:
            player2 = Player(p2, zero)
            self.players.append(player2)

        # player1 = Player("Nitish", cross)
        # player2 = Player("Vishal", zero)
        
        # self.players.append(player1)
        # self.players.append(player2)

        self.board = Board(3)

        print("Game has started now")

    def start_game(self):

        winner: bool = False

        while winner == False:
            
            # print the board
            self.board.print_board()

            # take the player whose turn is
            playerTurn = self.players.pop(0)

            # get the free space from the board
            free_spaces = self.board.free_cells()

            if len(free_spaces) == 0:
                winner = True # if no free space then, I've a winner
                continue

            # read the user input
            # print("Player: " + playerTurn.get_name() + " Enter row, column")
            coords = input("Player: " + playerTurn.get_name() + " Enter row, column: ")
            coords = coords.split(',')
            row, col = int(coords[0]), int(coords[1])


            # place the piece on that coordinates
            is_successfully_placed = self.board.add_piece(row, col, playerTurn.get_playing_piece())
            if is_successfully_placed == False:
               print("Incorrect position, Try again!")
               self.players.insert(0, playerTurn)
               continue

            # push the player in the list from the end for next turn
            self.players.append(playerTurn)

            # find the winner
            winner = self.find_winner(row, col, playerTurn.playingPiece.pieceType)
            if winner:
                # print("Yay, " + playerTurn.get_name() + " won the match!")
                return playerTurn.get_name()
        
        return "It's a tie"
    
    def find_winner(self, row: int, col: int, pieceType: PieceType):
        rowMatch = True
        colMatch = True
        onDiagonal = True
        offDiagonal = True


        # row check
        for i in range(0, self.board.size):
            if self.board[row][i] == None or self.board[row][i].pieceType != pieceType:
                rowMatch = False

        # col check
        for i in range(0, self.board.size):
            if self.board[i][col] == None or self.board[i][col].pieceType != pieceType:
                colMatch = False 

        # on-diagonal check
        j = 0
        for i in range(0, self.board.size):
            if self.board[i][j] == None or self.board[i][j].pieceType != pieceType:
                onDiagonal = False
            j += 1

        # off-diagonal check
        j = self.board.size-1 
        for i in range(0, self.board.size):
            if self.board[i][j] == None or self.board[i][j].pieceType != pieceType:
                offDiagonal = False
            j -= 1

        
        return rowMatch or colMatch or onDiagonal or offDiagonal

            