from GameFrame import Level, Globals
from Objects.InstructionManualTitle import InstructionManualTitle

class Missionsuccess (Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Missionsuccess.png")

        # add title object
        self.add_room_object(InstructionManualTitle(self, 20, 0))

        Globals.LIVES = 3
        Globals.SCORE = 0
        


       