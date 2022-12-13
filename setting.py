from os import path


WIN_WIDTH = 700
WIN_HEIGHT = 500

WIN_TEXT = 'YOU WIN'
WIN_COLOR = (15, 255, 20)
LOSE_TEXT = 'YOU LOSE'
LOSE_COLOR = (255, 0, 0)
WIN_TITLE = 'Shooter (Space wars)'
LABEL_WIN_COLOR = (255, 215, 100)
LABEL_MISSED_COLOR = (255, 111, 115)
LABEL_LEVEL_COLOR = (26, 122, 250)
LABEL_TIMER_COLOR = (226, 222, 50)

FPS = 50


FILE_DIR = path.dirname(__file__)

# AUDIOS
AUDIO_FILE_PATH = '%s/audio/' % FILE_DIR
MAIN_MUSIC_PATH = path.join(AUDIO_FILE_PATH, 'space.ogg')
EFFECT_MUSIC_PATH = path.join(AUDIO_FILE_PATH, 'fire.ogg')

# IMAGES:
IMG_FILE_PATH = '%s/img/' % FILE_DIR
ICON = path.join(IMG_FILE_PATH, 'icon.png')
IMG_BACK = path.join(IMG_FILE_PATH, 'galaxy.jpg')  # тло гри
IMG_BULLET = path.join(IMG_FILE_PATH, 'bullet.png')  # куля
IMG_HERO = path.join(IMG_FILE_PATH, 'rocket.png')  # герой
IMG_ENEMY = path.join(IMG_FILE_PATH, 'ufo.png')  # супротивник


SCORE = 0  # збито кораблів
GOAL = 10  # кількість кораблів, які необхідно збити для перемоги
LOST = 0  # пропущено кораблів
MAX_LOST = 3  # програли, якщо пропустили таку кількість
LEVEL = 1

PATH_FILE_STAT = 'game_stat.txt'
