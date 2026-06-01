from GameFrame import RoomObject, Globals
from Objects.Rock import Rock
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

        # start Rock timer
        Rock_spawn_time = random.randint(15,150)
        self.set_timer(Rock_spawn_time, self.spawn_Rock)

    def keep_in_room(self):
        """
        Keeps the Boss inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    
    def step(self):
        self.keep_in_room()

    def spawn_Rock(self):
        """
        Randomly spawns a new Rock
        """
        # spawn Rock and add to room
        new_Rock = Rock(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_Rock)
        
        # reset time for next Rock spawn
        Rock_spawn_time = random.randint(15, 150)
        self.set_timer(Rock_spawn_time, self.spawn_Rock)