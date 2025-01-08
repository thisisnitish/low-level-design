from models.playing_piece import PlayingPiece

class Player:
    name: str
    playingPiece: PlayingPiece

    def __init__(self, name: str, playingPiece: PlayingPiece):
        self.name = name
        self.playingPiece = playingPiece

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def get_playing_piece(self):
        return self.playingPiece
    
    def set_playing_piece(self, playingPiece: PlayingPiece):
        self.playingPiece = playingPiece