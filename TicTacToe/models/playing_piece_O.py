from models.playing_piece import PlayingPiece
from models.piece_type import PieceType

class PlayingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)
