class Player:
    img_file = "assets/Player.png"
    def __init__(self, x, y, width, height, world):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = 0
        self.y_speed = 0
        self.world = world
        self.rect = None
        self.image = None
        self.flip = False
        self.is_standing = False
    
    def move_right(self):
        delta_x = 10
        self.flip = False
        if self.rect.right + delta_x > self.world.width:
            delta_x = self.world.width - self.rect.right
        self.rect.x += delta_x
    
    def move_left(self):
        delta_x = -10
        self.flip = True
        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
        self.rect.x += delta_x
    
    def jump(self):
        if self.is_standing: 
            self.y_speed = -20
            self.is_standing = False

    def fall(self):
        self.y_speed += self.world.gravity
        delta_y = self.y_speed

        if self.rect.bottom + delta_y > self.world.height:
            delta_y = self.world.height - self.rect.bottom
            self.is_standing = True
        if self.rect.top + delta_y < 0:
            delta_y = -self.rect.top
            self.y_speed = 0
        self.rect.y += delta_y
    # def player_move(self, key)
    
    def set_rect(self, rect):
        self.rect = rect
        self.rect.center = (self.x, self.y)
    
    def set_image(self, image):
        self.image = image
        
    def get_rect(self):
        return self.rect
    
    def get_image(self):
        return self.image
    
    def set_rect_center(self, x, y):
        self.rect.center = (x, y)