from GameFrame import Level
from Objects.Title4 import Title4

class InstructionManual (Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("InstructionManual.png")

        # add title object
        self.add_room_object(Title4(self, 20, 0))

       