from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 45, 15)
        
        # set movement
        self.set_direction(0, 20)

        # handle events
        self.register_collision_object("Rock")
        self.register_collision_object("Python")
        self.register_collision_object("IDLE")
        
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

            
    # --- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Rock":
            self.room.delete_object(other)
            self.room.score.update_score(1)
        elif other_type == "Python":
            self.room.delete_object(other)
            self.room.score.update_score(-1)
        elif other_type == "IDLE":
            self.room.delete_object(other)
        self.room.delete_object(self)
        