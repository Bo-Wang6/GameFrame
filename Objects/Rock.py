from GameFrame import RoomObject

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