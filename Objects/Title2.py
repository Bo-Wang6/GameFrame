from GameFrame import RoomObject

class Title2(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Title2.png")
        self.set_image(image,500,50)