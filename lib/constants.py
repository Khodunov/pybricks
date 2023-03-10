# Масштаб
SCALE = 1

# Параметры кирпича
BRICK_HEIGHT = 66 * SCALE
BRICK_STARTING_X = 250 * SCALE
BRICK_STARTING_Y = 300 * SCALE
SPEED_Y = 100 * SCALE
BRICK_WIDTH = 194 * SCALE

# Параметры экрана и пола
SCREEN_WIDTH = 640 * SCALE
SCREEN_HEIGHT = 1000 * SCALE
FLOOR_HEIGHT = SCREEN_HEIGHT - 120 * SCALE
BRICK_STOP_HEIGHT = FLOOR_HEIGHT - BRICK_HEIGHT

# Ось и циферки
AXIS_COLOR = (130, 100, 50)
LINE_WIDTH = 5 * SCALE
TICK_LENGTH = 15 * SCALE
FONT_SIZE = int(30 * SCALE)

# Параметры руки
HAND_STARTING_X = 320 * SCALE
HAND_STARTING_Y = -1 * SCALE
HAND_SPEED_X = 100 * SCALE
HAND_SPEED_Y = 20 * SCALE
HAND_ACCELERATION = 1 * SCALE
MAX_HAND_SPEED = 500 * SCALE
HAND_GRIP_POSITION_X = -55 * SCALE
HAND_GRIP_POSITION_Y = 200 * SCALE

# Физические константы
FPS = 60
G = 800 * SCALE
DELTA_T = 1/FPS

# Картинки
IMAGES_DIRECTORY = "source/images/"
WHITE_BRICK_FILENAME = IMAGES_DIRECTORY + "brick_white.png"
BACKGROUND_FILENAME = IMAGES_DIRECTORY + "wallpaper_cut.jpg"
FLOOR_FILENAME = IMAGES_DIRECTORY + "floor.png"
HAND_FILENAME = IMAGES_DIRECTORY + "lego_hand.png"

# Звуки
SOUND_DIRECTORY = "source/sounds/"
BACK_MUSIC_1 = SOUND_DIRECTORY + "Back_music_1.mp3"
BUM_1 = SOUND_DIRECTORY + "Bym_1.mp3"
