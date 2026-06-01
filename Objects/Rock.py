from GameFrame import RoomObject, Globals
import random

class Rock(RoomObject):
    """
    A class for Boss danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Rock object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Rock.png")
        self.set_image(image,60,60)

        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, 10)

        # register events
        self.register_collision_object("Ship")

    def step(self):
        """
        Determines what happens to the Rock on each tick of the game clock
        """
        self.keep_in_room()
        
    def keep_in_room(self):
        """
        Keeps the Rock inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Rock
        """
        
        if other_type == "Ship":
            self.room.running = False