from player import behavior
import pygame, random

lvl1 = ['001111000000000000000000',
        '001001111111111111000000',
        '000000000000000000000000',
        '000000000000000000000000',
        '001001111111111111110011',
        '001000000001000001000000',
        '001000000001000001000000',
        '001001111111110001000000',
        '001000000000000011111000',
        '001000000000000010001000',
        '001111111111100010001030',
        '001000000000100010001000',
        '001000000000100110001000',
        '111111111100100010000000',
        '000000000000100010000000',
        '000000000000100011001111',
        '000000100000100010000000',
        '000000100000000010000200',
        '111100100000000010000000',
        '000000111111111110000000',
        '000000000000000010000000']



# 24, 20

blocks = []
money = None
img_money = pygame.image.load('gem.png')

def make_map(lvl:list):
    global blocks, money

    block_size = 25
    block_x = 0
    block_y = 0
    block_img = pygame.image.load('wall.png')

    for row in lvl:
        for tile in row:       
            if tile == '1':
                blocks.append(behavior(block_x, block_y, block_size, block_size, block_img))
            elif tile == '2':
                money = behavior(block_x, block_y, block_size*2 ,block_size*2, img_money)
            block_x += block_size
        block_x = 0
        block_y += block_size

    return (blocks, money)
