from GameFrame import Level,Globals
from Objects.GameoverTitle import GameoverTitle

class Gameover (Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Over.png")

        # add title object
        self.add_room_object(GameoverTitle(self, 20, 0))

        Globals.LIVES = 3
        Globals.SCORE = 0