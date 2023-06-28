from pygame import draw, Surface, Rect, transform
from .object import Object
class Player(Object):
    img_file = "assets/Player.png"
    def __init__(self, x, y, width, height, world):
        super().__init__(x, y, width, height, self.img_file)
        self.world = world
        self.flip = False
        self.is_standing = False
        self.y_speed = 0
        self.x_speed = 0
        self.rect = Rect(0, 0, 35, 80)

    def draw_player(self, screen: Surface):
        screen.blit(transform.flip(self.image, self.flip, False), (self.get_rect().x, self.get_rect().y-15))
        draw.rect(screen, (255, 255, 255), self.rect, 2)
    
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
    def get_down(self):
        if self.is_standing and self.rect.bottom < self.world.height:
            self.rect.y += 4
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
        for platform in self.world.get_platforms():
            if platform.rect.colliderect(self.rect.x, self.rect.y + delta_y, self.rect.width, self.rect.height):
                if self.rect.bottom <= platform.rect.top and self.rect.bottom + delta_y >= platform.rect.top:
                    delta_y = platform.rect.top - self.rect.bottom
                    self.is_standing = True
                    self.y_speed = 0
                # delta_y = platform.rect.top - self.rect.bottom
                # self.is_standing = True
                # self.y_speed = 0
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