from models.piece_type import PieceType

class PlayingPiece:
    pieceType: PieceType

    def __init__(self, pieceType: PieceType):
        self.pieceType = pieceType