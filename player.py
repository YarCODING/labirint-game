import pygame

class sprite:
    def __init__(self, x:int, y:int, w:int, h:int, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = image
        self.image = pygame.transform.scale(image, (w, h))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 2

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PLAYER(sprite):
    def __init__(self, x, y, w, h, speed, image):
        super().__init__(x, y, w, h, image)
        self.speed = speed

        self.direction = 'right'

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
    
class ENEMY(sprite):
    def __init__(self, x, y, w, h, image_right, speed, x2, direction = 'right'):
        super().__init__(x, y, w, h, image_right)
        self.image_left =  pygame.transform.scale(pygame.transform.flip(image_right, True, False), (w, h))
        self.image_right = pygame.transform.scale(image_right, (w, h))
        self.image = self.image_right
        self.speed = speed
        self.x1 = x
        self.x2 = x2

        self.direction = direction

    def move(self):
        if self.rect.x >= self.x2:
            self.rect.x = self.x2
            self.direction = 'left'
            self.image = self.image_left
        elif self.rect.x <= self.x1:
            self.rect.x = self.x1
            self.direction = 'right'
            self.image = self.image_right
        
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


player_img = pygame.image.load('ork.png')
enemy_img = pygame.image.load('knight.png')
player = PLAYER(0, 400, 30, 37, 5, player_img)
enemy = ENEMY(0, 52, 38, 47, enemy_img, 5, 650)