import pygame as pg

from lib.constants import DELTA_T, SCREEN_HEIGHT, G, WHITE_BRICK_FILENAME, \
    BRICK_STOP_HEIGHT


class Brick:

    def __init__(self, position, speed, sound_manager):
        self.position = list(position)
        self.speed = list(speed)
        self.sound_manager = sound_manager

        self.image = pg.image.load(WHITE_BRICK_FILENAME)

    def move(self):
        self.position[1] += self.speed[1] * DELTA_T
        if self.position[1] >= BRICK_STOP_HEIGHT:
            if self.speed[1] != 0:
                self.sound_manager.play_sound("explosion")
            self.speed[1] = 0
            self.position[1] = BRICK_STOP_HEIGHT
        else:
            self.speed[1] += G * DELTA_T



