import pygame as pg

from lib.brick import Brick
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()

background_image = pg.image.load("source/images/wallpaper_cut.jpg")

brick_x = 250
brick_y = 300
speed_y = 100
brick = Brick(position=(brick_x, brick_y),
              speed=(0, speed_y))

while True:
    screen.blit(background_image, (0, 0))
    screen.blit(brick.image, brick.position)

    brick.move()

    pg.display.update()
    clock.tick(FPS)



