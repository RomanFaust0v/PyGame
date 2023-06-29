from pygame import draw, Surface, Rect, transform
from baseObject import Object
class Player(Object):
    img_file = "assets/Player.png"
    def __init__(self, x, y, width, height, world):
        super().__init__(x, y, width, height, self.img_file)
        self.world = world
        self.flip = False
        self.is_standing = False
        self.can_fall = True
        self.y_speed = 0
        self.x_speed = 0
        self.rect = Rect(self.x, self.y, 40, 60)
        self.standing_on = None

    def draw_player(self, screen: Surface):
        screen.blit(transform.flip(self.image, self.flip, False), (self.get_rect().x, self.get_rect().y-15))
        # draw.rect(screen, (255, 255, 255), self.rect, 2)
    
    def move_right(self):
        if self.x_speed < 8 and self.x_speed >= 0:
            self.x_speed += 1
        elif self.x_speed == 8:
            self.x_speed -= 1
        else:
            return
        delta_x = self.x_speed
        self.flip = False
        if self.rect.right + delta_x > self.world.width:
            delta_x = self.world.width - self.rect.right
        for platform in self.world.get_platforms():
            if platform.rect.colliderect(self.rect.x + delta_x, self.rect.y, self.rect.width, self.rect.height):
                if self.rect.right <= platform.rect.left and self.rect.right + delta_x >= platform.rect.left:
                    delta_x = platform.rect.left - self.rect.right
        self.rect.x += delta_x
    
    def move_left(self):
        if self.x_speed > -8 and self.x_speed <= 0:
            self.x_speed -= 1
        elif self.x_speed == -8:
            self.x_speed += 1
        else:
            return
        delta_x = self.x_speed
        self.flip = True
        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
        for platform in self.world.get_platforms():
            if platform.rect.colliderect(self.rect.x + delta_x, self.rect.y, self.rect.width, self.rect.height):
                if self.rect.left >= platform.rect.right and self.rect.left + delta_x <= platform.rect.right:
                    delta_x = platform.rect.right - self.rect.left
        self.rect.x += delta_x
    
    def jump(self):
        if self.is_standing: 
            self.y_speed = -20
            self.is_standing = False
    
    def get_down(self):
        if self.is_standing and self.rect.bottom < self.world.height and self.can_fall:
            self.rect.y += 4
            self.is_standing = False
    
    def fall(self):
        self.is_standing = False
        self.standing_on = None
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
                    self.standing_on = platform
                    break
                elif self.rect.top >= platform.rect.bottom and self.rect.top + delta_y <= platform.rect.bottom:
                    delta_y = platform.rect.bottom - self.rect.top
                    self.y_speed = 0
                # delta_y = platform.rect.top - self.rect.bottom
                # self.is_standing = True
                # self.y_speed = 0
        if self.is_standing:
            grid_x = self.rect.x // self.standing_on.width
            grid_y = self.standing_on.y // self.standing_on.height + 1
            if self.rect.x % self.standing_on.width:
                for i in range(2):
                    if self.world.level[grid_y+i][grid_x] == "#" or self.world.level[grid_y+i][grid_x+1] == "#":
                        self.can_fall = False
                        break
                    else:
                        self.can_fall = True
            else:
                if self.world.level[grid_y][grid_x] == "#" or self.world.level[grid_y + 1][grid_x] == "#":
                    self.can_fall = False
                else:
                    self.can_fall = True
        self.rect.y += delta_y
        
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
    
    def set_x_speed(self, x_speed):
        self.x_speed = x_speed