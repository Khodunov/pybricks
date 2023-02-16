import sys

import pygame as pg

from lib.background import Background
from lib.brick import Brick
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, HAND_STARTING_X, \
    HAND_STARTING_Y, HAND_SPEED_X, HAND_SPEED_Y, BRICK_STARTING_X, \
    BRICK_STARTING_Y, SPEED_Y
from lib.game_manager import GameManager
from lib.hand import Hand
from lib.sound import SoundManager


def get_all_keydowns():
    all_keydowns = []

    events = pg.event.get()
    for event in events:
        # Проверка на выход из игры
        need_to_exit = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                need_to_exit = True
            else:
                all_keydowns.append(event.key)
        if event.type == pg.QUIT:
            need_to_exit = True
        if need_to_exit:
            pg.quit()
            sys.exit()

    return all_keydowns

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
sound_manager = SoundManager()
game_manager = GameManager(sound_manager=sound_manager)

while True:
    keydowns = get_all_keydowns()
    game_manager.update(keydowns)
    game_manager.draw(screen)

    pg.display.update()
    clock.tick(FPS)

















