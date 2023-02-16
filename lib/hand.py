# Здесь будут все связанные с рукой моменты

import pygame as pg

from lib.constants import DELTA_T, SCREEN_WIDTH, HAND_ACCELERATION, \
    MAX_HAND_SPEED, SCREEN_HEIGHT


class Hand:
    def __init__(self, position, speed):
        self.position = list(position)
        self.speed = list(speed)

        self.image = pg.image.load("source/images/lego_hand.png")

    def move(self):
        self.position[0] += self.speed[0] * DELTA_T
        if 0 < self.speed[0] < MAX_HAND_SPEED:
            self.speed[0] += HAND_ACCELERATION
        if -MAX_HAND_SPEED < self.speed[0] < 0:
            self.speed[0] -= HAND_ACCELERATION
        if not (SCREEN_WIDTH * 0.05 < self.position[0] < SCREEN_WIDTH * 0.8):
            self.speed[0] *= -1

        self.position[1] += self.speed[1] * DELTA_T
        if self.position[1] <= - SCREEN_HEIGHT * 0.15:
            self.speed[1] *= -1
        if self.position[1] >= 0:
            self.speed[1] *= -1
