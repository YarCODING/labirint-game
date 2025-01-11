import pygame
from player import player, enemy
from maps import*

pygame.init()

size = (600, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Labirint')

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, size)


pygame.mixer.music.load('music.ogg')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

make_map(lvl1)

game = True
while game:
    window.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.move(size)
    player.draw(window)

    enemy.move(size)
    enemy.draw(window)

    for block in blocks:
        block.draw(window)


    clock.tick(FPS)
    pygame.display.flip()