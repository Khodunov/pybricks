import pygame as pg

from lib.background import Background
from lib.brick import BrickManager
from lib.constants import HAND_STARTING_X, HAND_STARTING_Y, HAND_SPEED_X, \
    HAND_SPEED_Y, BRICK_STARTING_X, BRICK_STARTING_Y, SPEED_Y
from lib.hand import Hand
from lib.camera import Camera


class GameManager:

    def __init__(self, sound_manager):
        self.sound_manager = sound_manager
        self.camera = Camera()

        self.hand = Hand(position=(HAND_STARTING_X, HAND_STARTING_Y),
                         speed=(HAND_SPEED_X, HAND_SPEED_Y))
        self.brick_manager = BrickManager(hand=self.hand,
                                          sound_manager=self.sound_manager,
                                          camera=self.camera)

        self.background = Background()

        sound_manager.play_music("back_music")

    def draw(self, surface):
        self.background.draw_game_window(surface, self.camera.current_scroll)
        self.brick_manager.draw_bricks(surface, self.camera.current_scroll)
        self.hand.draw(surface)

    def update(self, pressed_keys):
        self.hand.move()
        new_state = self.brick_manager.move(pressed_keys)
        if new_state == "menu":
            self.__init__(sound_manager=self.sound_manager)
        return new_state
