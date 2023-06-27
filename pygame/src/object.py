from pygame import image, transform, Rect, display, Surface, draw
class Object():
    
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(image_path), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw_object(self, screen: Surface):
        screen.blit(self.image, self.rect)
        