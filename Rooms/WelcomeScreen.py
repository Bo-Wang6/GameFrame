from GameFrame import Level
from Objects.WelcomeScreenTitle import WelcomeScreenTitle
from Objects.WelcomeScreenTitle2 import WelcomeScreenTitle2

class WelcomeScreen(Level):
    """
    Intial screen for the game
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image（from gpt）
        self.set_background_image("Background.png")

        # add title object
        self.add_room_object(WelcomeScreenTitle(self, 20, 0))

        self.add_room_object(WelcomeScreenTitle2(self, 400, 400))

        # load sounds
        self.bg_music = self.load_sound("Music.mp3")
        
        # play background music
        self.bg_music.set_volume(0.4)
        self.bg_music.play(loops=1)

        