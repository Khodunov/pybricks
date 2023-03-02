import sys
import pygame as pg

from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from lib.game_manager import GameManager
from lib.sound import SoundManager


def get_all_pressed_keys():
    pressed_keys = []

    events = pg.event.get()
    for event in events:
        # Проверка на выход из игры
        need_to_exit = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                need_to_exit = True
            else:
                pressed_keys.append(event.key)
        if event.type == pg.QUIT:
            need_to_exit = True
        if need_to_exit:
            pg.quit()
            sys.exit()

    return pressed_keys


pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pg.time.Clock()
sound_manager = SoundManager()
game_manager = GameManager(sound_manager=sound_manager)

while True:
    keys = get_all_pressed_keys()
    game_manager.update(pressed_keys=keys)
    game_manager.draw(surface=screen)

    pg.display.update()
    clock.tick(FPS)

















