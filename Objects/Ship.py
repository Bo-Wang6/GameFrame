from GameFrame import RoomObject
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)

        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up, down, left and right
        """
        
        if key[pygame.K_w]:
            self.y -= 7.5
        elif key[pygame.K_s]:
            self.y += 7.5
        if key[pygame.K_a]:
            self.x -= 7.5
        elif key[pygame.K_d]:
            self.x += 7.5
        