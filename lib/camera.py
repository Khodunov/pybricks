from lib.constants import BRICK_HEIGHT


class Camera:
    def __init__(self):
        self.current_scroll = 0

    def camera_up (self):
        self.current_scroll += BRICK_HEIGHT


