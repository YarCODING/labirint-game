import pygame
from player import*
from maps import*

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# сделать ещё одну карту которая будет ставиться при нажатии кнопки (каждая карта не проходима по отдельности)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!

pygame.init()

size = (600, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Labirint')

FPS = 30
clock = pygame.time.Clock()

bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, size)


pygame.mixer.music.load('music.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

losemusic = pygame.mixer.Sound("lose_music.mp3")
losemusic.set_volume(0.4)
winmusic = pygame.mixer.Sound('win_music.mp3')


blocks, money = make_map(lvl1)


font = pygame.font.SysFont('Arial', 40, True)
font_small = pygame.font.SysFont('Arial', 20)
lose = font.render('You lose!', True, (255, 0, 0))
continui = font_small.render('(Щоб почати спочатку натисніть пробіл)', True, (255, 0, 0))
win = font.render('You win!', True, (0, 255, 0))

game = True
finish = False

while game:

    if not finish:
        window.blit(bg, (0,0))


        money.draw(window)

        player.move(size)
        player.draw(window)

        enemy.move(size)
        enemy.draw(window)

        for block in blocks:
            block.draw(window)
        
        for b in blocks:
            if player.rect.colliderect(b.rect):
                finish = True
                pygame.mixer.music.stop()
                losemusic.play(-1)
                window.blit(lose, (210, 250))
                window.blit(continui, (140, 300))

        if player.rect.colliderect(money.rect):
            pygame.mixer.music.stop()
            winmusic.play(-1)
            finish = True
            window.blit(win, (210, 250))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and finish == True:
            finish = False
            player = PLAYER(0, 400, 30, 37, 5, player_img)
            winmusic.stop()
            losemusic.stop()
            pygame.mixer.music.play()


    pygame.display.flip()
    clock.tick(FPS)

pygame.time.delay(1000)