import pygame 

class Entity(pygame.sprite.DirtySprite):
    def __init__(self, x, y, picture_path):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(picture_path).convert_alpha()   
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        

    def update(self):
        self.rect.center = self.x, self.y
        

    def DestroyEntity(self):
        pygame.sprite.Sprite.kill(self)

    def swapSprite(self, img):
        self.image = pygame.image.load(img).convert_alpha()  

    def Scale(self, scaleFactor):
        self.scaleFactor = scaleFactor
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*self.scaleFactor), int(self.size[1]*self.scaleFactor)))
        self.image = self.bigger_img

class AnimatedEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, animArray, speed):
        super().__init__()
        self.speed = speed
        self.sprites = animArray
        self.currentSprite = 0
        self.isAnimating = False
        self.image = self.sprites[self.currentSprite]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        
    def animate(self):
        self.isAnimating = True
    
    def update(self):
        self.rect.center = self.x, self.y
        if self.isAnimating == True:
            self.currentSprite += self.speed

            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
                self.isAnimating = False

            self.image = self.sprites[int(self.currentSprite)]
    
    def Scale(self, scaleFactor):
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0]*scaleFactor), int(self.size[1]*scaleFactor)))
        self.image = self.bigger_img

    def Flip(self):
        self.flipped_img = pygame.transform.flip(self.image, True, False)
        self.image = self.flipped_img


