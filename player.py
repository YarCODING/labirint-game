import pygame

class behavior:
    def __init__(self, x:int, y:int, w:int, h:int, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = image
        self.image = pygame.transform.scale(image, (w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 10

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PLAYER(behavior):
    def __init__(self, x, y, w, h, speed, image):
        super().__init__(x, y, w, h, image)
        self.speed = speed


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, size):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.rect.x < size[0] - self.h:
            self.rect.x += self.speed
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < size[1] - self.h:
            self.rect.y += self.speed
    
class ENEMY(behavior):
    def __init__(self, x, y, w, h, image):
        super().__init__(x, y, w, h, image)
        self.aggresion = 1
        self.speed = 5 * self.aggresion

    def move(self, size):
        pass
        

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))



player_img = pygame.image.load('ork.png')
enemy_img = pygame.image.load('knight.png')
player = PLAYER(0, 400, 45, 54, 5, player_img)
enemy = ENEMY(500, 0, 45, 54, enemy_img)