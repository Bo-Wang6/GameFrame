from GameFrame import RoomObject, Globals
import random

class IDLE(RoomObject):
    """
    A class for IDLE
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the IDLE object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("IDLE.png")
        self.set_image(image,50,49)
        
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
        self.outside_of_room()
        
    def keep_in_room(self):
        """
        Keeps the IDLE inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1
            
    def outside_of_room(self):
        """
        removes IDLE that have exited the room
        """
        if self.x + self.width < 0:
            print("IDLE deleted")
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the IDLE
        """
        
        if other_type == "Ship":
            self.room.astronaut_saved.play()
            Globals.LIVES += 1
            other.room.delete_object(self)
            if Globals.LIVES < 4:
                self.room.lives.update_image()
            if Globals.LIVES > 3:
                Globals.LIVES = 3
                self.room.score.update_score(1)
            # if Globals.LIVES > 0:
            #     self.room.running = False



           