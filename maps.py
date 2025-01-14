from player import behavior
import pygame, random

lvl1 = ['000001000000000000000000',
        '000001111111110000000000',
        '000001000000000001000000',
        '000001000000000001000000',
        '000001000001000001000000',
        '000001111111000001000000',
        '000000000001000001000000',
        '001111111111110011100000',
        '001000000000000010000000',
        '001000000000000010000000',
        '001111111001000010000000',
        '001000010001000010000000',
        '001000010001111110000000',
        '000001110000100010000000',
        '000000000000100010000000',
        '000000000000100010000000',
        '000000100000100010000000',
        '000000100000100010000200',
        '111100100000000010000000',
        '000000111111111110000000',
        '000000000000100000000000',]


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
