from GameFrame import Level
from Objects.Title import Title
from Objects.Title2 import Title2

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Background.png")

        # add title object
        self.add_room_object(Title(self, 20, 0))

        self.add_room_object(Title2(self, 400, 400))