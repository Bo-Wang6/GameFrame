from GameFrame import Level,Globals
from Objects.Title3 import Title3

class Test (Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Over.png")

        # add title object
        self.add_room_object(Title3(self, 20, 0))

        Globals.LIVES = 3
        Globals.SCORE = 0