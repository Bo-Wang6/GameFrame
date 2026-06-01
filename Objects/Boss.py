from GameFrame import RoomObject, Globals
import random

class Boss (RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Boss.png")
        self.set_image(image,165,165)

        # set inital movement
        self.y_speed = random.choice([-7.5,7.5])

    def keep_in_room(self):
        """
        Keeps the Boss inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    
    def step(self):
        self.keep_in_room()