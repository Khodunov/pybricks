import pygame as pg

from lib.constants import SCREEN_HEIGHT, FLOOR_HEIGHT, AXIS_COLOR, \
    BRICK_HEIGHT, BACKGROUND_FILENAME, FLOOR_FILENAME, TICK_LENGTH, LINE_WIDTH


class Background:
    def __init__(self):
        self.fon_image = pg.image.load(BACKGROUND_FILENAME)
        self.floor_image = pg.image.load(FLOOR_FILENAME)

        self.axis_font = pg.font.Font(None, 30)

    def draw_game_window(self, surface, scroll):
        surface.blit(self.fon_image, (0, 0))
        self.draw_axis(surface, scroll)
        self.draw_floor(surface, scroll)

    def draw_floor(self, surface, scroll):
        # drawing a rect back on floor image for your perfekcionizm eyes
        pg.draw.rect(surface, AXIS_COLOR, (0, FLOOR_HEIGHT + scroll, 10, 20))
        surface.blit(self.floor_image, (0, FLOOR_HEIGHT + scroll))

    def draw_axis(self, surface, scroll):  # text on axis and axis
        ticks_below = 5
        first_tick = (SCREEN_HEIGHT - FLOOR_HEIGHT) - \
                     BRICK_HEIGHT * ticks_below
        for i in range(int(scroll / BRICK_HEIGHT) - ticks_below,
                       int(scroll / BRICK_HEIGHT) + 15):
            pg.draw.rect(surface, AXIS_COLOR, (
                0, SCREEN_HEIGHT - first_tick, LINE_WIDTH,
                BRICK_HEIGHT))  # neposredstvenno axis

            if i > 0:
                pg.draw.line(surface, AXIS_COLOR,
                             [0, SCREEN_HEIGHT - first_tick],
                             [TICK_LENGTH, SCREEN_HEIGHT - first_tick],
                             int(LINE_WIDTH * 0.8))

                axis_text = self.axis_font.render(str(i), True,
                                                  AXIS_COLOR)  # ciferki
                surface.blit(axis_text, (int(TICK_LENGTH * 1.2),
                             SCREEN_HEIGHT - first_tick - int(LINE_WIDTH*1.6)))

            first_tick += BRICK_HEIGHT







