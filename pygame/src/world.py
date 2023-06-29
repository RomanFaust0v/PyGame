from baseObject import Object

class World(Object):
    bckgr_img = "assets/background.png"
    def __init__(self, width, height, x, y):
        super().__init__(x, y, width, height, self.bckgr_img)
        self.gravity = 1
        self.max_platforms = 30
        self.platforms = None
        self.level = None
    
    def set_background(self, background):
        self.image = background
    
    def get_background(self):
        return self.image

    def get_max_platforms(self):
        return self.max_platforms
    
    def set_max_platforms(self, max_platforms):
        self.max_platforms = max_platforms
    
    def get_gravity(self):
        return self.gravity
    
    def set_gravity(self, gravity):
        self.gravity = gravity
    
    def set_platforms(self, platforms):
        self.platforms = platforms
    
    def get_platforms(self):
        return self.platforms
    
    def set_level(self, level):
        self.level = level