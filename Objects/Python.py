from GameFrame import RoomObject

class Python(RoomObject):
    """
    Class for the Python escaping from Zork
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the Python instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Python.png")
        self.set_image(image,50,49)
        
        # set travel direction
        self.set_direction(180, 5)
        
        # handle events
        self.register_collision_object("Ship")
        
    def step(self):
        """
        Determines what happend to the Python on each tick of the game clock
        """
        self.outside_of_room()
        
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Python objects
        """
        # ship collision
        if other_type == "Ship":
            self.room.astronaut_saved.play()
            self.room.delete_object(self)
            self.room.score.update_score(2)
            
    def outside_of_room(self):
        """
        removes Python that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
            