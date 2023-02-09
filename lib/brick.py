import pygame as pg

from lib.constants import DELTA_T, SCREEN_HEIGHT, G


class Brick:

    def __init__(self, position, speed):
        self.position = list(position)
        self.speed = list(speed)

        self.image = pg.image.load("source/images/brick_white.png")

    def move(self):
        self.position[1] += self.speed[1] * DELTA_T
        if self.position[1] >= SCREEN_HEIGHT * 0.8:
            self.speed[1] = 0
            self.position[1] = SCREEN_HEIGHT * 0.8
        else:
            self.speed[1] += G * DELTA_T



