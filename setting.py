from os import path


WIN_WIDTH: int = 700
WIN_HEIGHT: int = 500

WIN_TEXT: str = 'YOU WIN'
WIN_COLOR: tuple = (15, 255, 20)
LOSE_TEXT: str = 'YOU LOSE'
LOSE_COLOR: tuple = (255, 0, 0)
WIN_TITLE: str = 'Shooter (Space wars)'
LABEL_WIN_COLOR: tuple = (255, 215, 100)
LABEL_MISSED_COLOR: tuple = (255, 111, 115)
LABEL_LEVEL_COLOR: tuple = (26, 122, 250)
LABEL_TIMER_COLOR: tuple = (226, 222, 50)

FPS: int = 50


FILE_DIR: str = path.dirname(__file__)

# AUDIOS
AUDIO_FILE_PATH: str = '%s/audio/' % FILE_DIR
MAIN_MUSIC_PATH: str = path.join(AUDIO_FILE_PATH, 'space.ogg')
EFFECT_MUSIC_PATH: str = path.join(AUDIO_FILE_PATH, 'fire.ogg')

# IMAGES:
IMG_FILE_PATH: str = '%s/img/' % FILE_DIR
ICON: str = path.join(IMG_FILE_PATH, 'icon.png')
IMG_BACK: str = path.join(IMG_FILE_PATH, 'galaxy.jpg')  # тло гри
IMG_BULLET: str = path.join(IMG_FILE_PATH, 'bullet.png')  # куля
IMG_HERO: str = path.join(IMG_FILE_PATH, 'rocket.png')  # герой
IMG_ENEMY: str = path.join(IMG_FILE_PATH, 'ufo.png')  # супротивник


SCORE: int = 0  # збито кораблів
GOAL: int = 10  # кількість кораблів, які необхідно збити для перемоги
LOST: int = 0  # пропущено кораблів
MAX_LOST: int = 3  # програли, якщо пропустили таку кількість
LEVEL: int = 1

PATH_FILE_STAT = 'game_stat.txt'
