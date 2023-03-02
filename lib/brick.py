import sys
from copy import copy

import pygame as pg

from lib.constants import DELTA_T, G, WHITE_BRICK_FILENAME, \
    BRICK_STOP_HEIGHT, BRICK_HEIGHT, BRICK_WIDTH, HAND_GRIP_POSITION_X, \
    HAND_GRIP_POSITION_Y, SCALE
from lib.utilities import scale_image


class Brick:

    def __init__(self, position, speed, sound_manager, state="in_hand"):
        self.state = state
        self.position = list(position)
        self.speed = list(speed)
        self.sound_manager = sound_manager

        self.image = pg.image.load(WHITE_BRICK_FILENAME)
        self.image = scale_image(self.image, SCALE)

    def move(self, hand_position, bricks_count, scroll):
        if self.state == "in_hand":
            self.position = list(hand_position)
            self.position[0] += HAND_GRIP_POSITION_X
            self.position[1] += HAND_GRIP_POSITION_Y
            self.position[1] -= scroll
        if self.state == "falling":
            self.position[1] += self.speed[1] * DELTA_T
            if self.position[1] >= BRICK_STOP_HEIGHT - (bricks_count - 1) * \
                    BRICK_HEIGHT:
                if self.speed[1] != 0:
                    self.sound_manager.play_sound("explosion")
                self.speed[1] = 0
                self.position[1] = BRICK_STOP_HEIGHT - (bricks_count - 1) * \
                                   BRICK_HEIGHT
                self.state = "rest"
            else:
                self.speed[1] += G * DELTA_T

    def draw(self, surface, scroll):
        scrolled_position = copy(self.position)
        scrolled_position[1] += scroll
        surface.blit(self.image, scrolled_position)


class BrickManager:

    def __init__(self, hand, sound_manager, camera):
        self.sound_manager = sound_manager
        self.hand = hand
        self.camera = camera
        self.bricks = []
        self.new_brick()

    def new_brick(self):
        brick = Brick(position=(0, 0),
                      speed=(0, 0),
                      sound_manager=self.sound_manager)
        self.bricks.append(brick)

    def move(self, pressed_keys):
        if pg.K_SPACE in pressed_keys:
            self.bricks[-1].state = "falling"

        number_of_bricks = len(self.bricks)
        for brick in self.bricks:
            start_state = self.bricks[-1].state
            brick.move(hand_position=self.hand.position,
                       bricks_count=number_of_bricks,
                       scroll=self.camera.current_scroll)
            next_state = self.bricks[-1].state
            if start_state != next_state and next_state != "falling":
                if number_of_bricks >= 2:
                    active_brick = self.bricks[-1]
                    active_brick_center = active_brick.position[0] + \
                                          BRICK_WIDTH/2
                    top_brick_left = self.bricks[-2].position[0]
                    top_brick_right = self.bricks[-2].position[0] + BRICK_WIDTH
                    if active_brick.state == "rest" and not \
                            (top_brick_left < active_brick_center <
                             top_brick_right):
                        return "menu"
                self.new_brick()
                if len(self.bricks) >= 6:
                    self.camera.camera_up()

        return "game"

    def draw_bricks(self, screen, scroll):
        for brick in self.bricks:
            brick.draw(screen, scroll)


