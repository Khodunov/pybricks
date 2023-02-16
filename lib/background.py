import pygame as pg

from lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT, \
    AXIS_COLOR, BRICK_HEIGHT, BACKGROUND_FILENAME, FLOOR_FILENAME


class Background:
    def __init__(self):
        self.fon_image = pg.image.load(BACKGROUND_FILENAME)
        self.floor_image = pg.image.load(FLOOR_FILENAME)

        self.axis_font = pg.font.Font(None, 30)

    def draw_game_window(self, surface):
        self.draw_background(surface)
        self.draw_axis(surface)

    def draw_background(self, surface):
        # fon and floor
        surface.blit(self.fon_image, (0, 0))
        pg.draw.rect(surface, AXIS_COLOR, (0, FLOOR_HEIGHT, 10, 20))  # drawing a rect back on floor image for your perfekcionizm eyes
        surface.blit(self.floor_image, (0, FLOOR_HEIGHT))

    def draw_axis(self, surface):  # text on axis and axis
        first_otmetka = BRICK_HEIGHT
        for i in range(20):
            pg.draw.rect(surface, AXIS_COLOR, (0, FLOOR_HEIGHT - first_otmetka, 5, BRICK_HEIGHT)) # neposredstvenno axis
            pg.draw.line(surface, AXIS_COLOR, [0, FLOOR_HEIGHT - first_otmetka], [15, FLOOR_HEIGHT - first_otmetka],4)

            axis_text = self.axis_font.render(str(i), True, AXIS_COLOR) # ciferki
            surface.blit(axis_text, (18, FLOOR_HEIGHT - first_otmetka - 8))
            first_otmetka += BRICK_HEIGHT







