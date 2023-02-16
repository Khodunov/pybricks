import pygame as pg

from lib.background import Background
from lib.brick import Brick
from lib.constants import HAND_STARTING_X, HAND_STARTING_Y, HAND_SPEED_X, \
    HAND_SPEED_Y, BRICK_STARTING_X, BRICK_STARTING_Y, SPEED_Y
from lib.hand import Hand


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager

        self.bricks = []
        self.new_brick()
        self.hand = Hand(position=(HAND_STARTING_X, HAND_STARTING_Y),
                         speed=(HAND_SPEED_X, HAND_SPEED_Y))

        self.background = Background()

        sound_manager.play_music("back_music")

    def new_brick(self):
        brick = Brick(position=(BRICK_STARTING_X, BRICK_STARTING_Y),
                      speed=(0, SPEED_Y),
                      sound_manager=self.sound_manager)
        self.bricks.append(brick)

    def draw(self, surface):
        self.background.draw_game_window(surface)
        for brick in self.bricks:
            surface.blit(brick.image, brick.position)
        surface.blit(self.hand.image, self.hand.position)

    def update(self, keydowns):
        if pg.K_SPACE in keydowns:
            self.new_brick()

        for brick in self.bricks:
            brick.move()
        self.hand.move()
