from pygame.sprite import Group, Sprite
from object import Object
class Platform(Sprite, Object):
    plat_img_1 = "assets/Terrain1.png"
    plat_img_2 = "assets/Terrain2.png"
    
    def __init__(self, x, y, width, height):
        super().__init__()
        Object.__init__(self, x, y, width, height, self.plat_img_1)

