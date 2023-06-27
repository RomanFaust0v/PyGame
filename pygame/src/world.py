class World:
    bckgr_img = "assets/background.png"
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.gravity = 0.5
        self.background = None
    
    def set_background(self, background):
        self.background = background
    
    def get_background(self):
        return self.background
            