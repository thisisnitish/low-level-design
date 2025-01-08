from models.playing_piece import PlayingPiece

from typing import List

class Board:
    size: int = 0
    board: List[List[PlayingPiece]] = [[]]

    def __init__(self, size):
        self.size = size
        for _ in range(size):
            # col = [None]*size
            # self.board.append(col)
            self.board = [[None for _ in range(size)] for _ in range(size)]  # Initialize an empty board

    def __getitem__(self, index):
        return self.board[index]  # Allow indexing into the Board object
    
    def print_board(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if len(self.board[i]) > 0 and self.board[i][j] != None:
                    print(self.board[i][j].pieceType.value, end="")
                else:
                    print("     ", end="")
                print("  |  ", end="")    
            print()

    def free_cells(self):
        free_cells = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if len(self.board[i]) > 0 and self.board[i][j] == None:
                    free_cells.append((i, j))
                
        return free_cells
        

    def add_piece(self, row: int, col: int, playingPiece: PlayingPiece) -> bool:
                
        # check if that position is empty or not
        if self.board[row][col] is not None:
            return False
                
                
        self.board[row][col] = playingPiece
        return True

        
