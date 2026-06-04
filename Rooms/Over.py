from GameFrame import Level
from Objects.Title3 import Title3

class over (Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Mission Fail.png")