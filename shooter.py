import pygame
from pygame import *
from random import randint
from setting import *
import time


# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        """This is method init()"""
        # викликаємо конструктор класу (Sprite):
        super().__init__()

        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, який малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    """Клас головного гравця"""

    def update(self):
        """Метод для керування спрайтом стрілками клавіатури"""
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIN_WIDTH - 80:
            self.rect.x += self.speed

    def fire(self):
        """Метод "постріл" (використовуємо місце гравця, щоб створити там кулю)"""
        bullet = Bullet(IMG_BULLET, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    """Клас спрайту-супротивника"""
    def update(self):
        """Рух ворога"""
        self.rect.y += self.speed
        global LOST
        # зникає, якщо дійде до краю екрану
        if self.rect.y > WIN_HEIGHT:
            self.rect.x = randint(80, WIN_WIDTH - 80)
            self.rect.y = 0
            LOST += 1


class Bullet(GameSprite):
    """Клас спрайту-кулі"""
    def update(self):
        """Рух супротивника"""
        self.rect.y += self.speed
        # зникає, якщо дійде до краю екрану
        if self.rect.y < 0:
            self.kill()


class Statistics:
    def __init__(self, st_point_win=0, st_point_lose=0, duration=0, level=0):
        self._st_point_win = st_point_win
        self._st_point_lose = st_point_lose
        self._duration = duration
        self._level = level

    def __repr__(self):
        return f'{self._st_point_win} {self._st_point_lose} {self._duration} {self._level}'


def save_statistics(filename: str):
    with open(filename, 'w', encoding='UTF-8') as f:
        for row in stat:
            # print(type(row))
            # <class '__main__.Statistics'>
            f.write(str(row) + '\n')


# окремо підвантажуємо функції для роботи зі шрифтом
font.init()
font1 = font.Font(None, 80)
win = font1.render(WIN_TEXT, True, WIN_COLOR)
lose = font1.render(LOSE_TEXT, True, LOSE_COLOR)
font2 = font.Font(None, 36)

# фонова музика
mixer.init()
mixer.music.load(MAIN_MUSIC_PATH)
mixer.music.set_volume(0.1)
mixer.music.play(-1)
fire_sound = mixer.Sound(EFFECT_MUSIC_PATH)
fire_sound.set_volume(0.1)

# create window
display.set_icon(image.load(ICON))
display.set_caption(WIN_TITLE)
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
background = transform.scale(image.load(IMG_BACK), (WIN_WIDTH, WIN_HEIGHT))
TIMER = time.time()
# create sprites
ship = Player(IMG_HERO, 5, WIN_HEIGHT - 100, 80, 100, 10)
# створення групи спрайтів-ворогів
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(IMG_ENEMY, randint(80, WIN_WIDTH - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()


stat: list = []
# змінна "гра закінчилася": як тільки там True, в основному циклі перестають працювати спрайти
finish: bool = False
# основний цикл гри:
run: bool = True  # прапор скидається кнопкою закриття вікна
while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
        # подія натискання на пробіл - спрайт стріляє
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    # сама гра: дії спрайтів, перевірка правил гри, перемальовка
    if LEVEL < 1:
        run = False

    if not finish:
        # оновлюємо тло
        window.blit(background, (0, 0))

        # виробляємо рухи спрайтів
        ship.update()
        monsters.update()
        bullets.update()

        # оновлюємо їх у новому місці при кожній ітерації циклу
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        # перевірка зіткнення кулі та монстрів (і монстр, і куля при дотику зникають)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # цей цикл повториться стільки разів, скільки монстрів підбито
            SCORE += 1
            monster = Enemy(IMG_ENEMY, randint(80, WIN_WIDTH - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        # можливий програш: пропустили забагато чи герой зіткнувся з ворогом
        if sprite.spritecollide(ship, monsters, False) or LOST >= MAX_LOST:
            LEVEL -= 1
            finish = True  # програли, ставимо тло і більше не керуємо спрайтами.
            window.blit(lose, (200, 200))

        # перевірка виграшу: скільки очок набрали?
        if SCORE >= GOAL:
            LEVEL += 1
            finish = True
            window.blit(win, (200, 200))

        if LEVEL == 3:
            for c in collides:
                # цей цикл повториться стільки разів, скільки монстрів підбито
                SCORE += 1
                monster = Enemy(IMG_ENEMY, randint(80, WIN_WIDTH - 80), -40, 80, 50, randint(1, 7))
                monsters.add(monster)

        # пишемо текст на екрані
        text = font2.render("Total: " + str(SCORE), 1, (255, 215, 100))
        window.blit(text, (10, 20))

        text_lose = font2.render("Missed: " + str(LOST), 1, (255, 111, 115))
        window.blit(text_lose, (10, 50))

        text_level = font2.render("Level: " + str(LEVEL), 1, (26, 122, 250))
        window.blit(text_level, (310, 20))

        diff_timer = round(time.time() - TIMER, 2)
        text_timer = font2.render("Time: " + str(diff_timer) + 's', 1, (226, 222, 50))
        window.blit(text_timer, (500, 20))

        display.update()
    # автоматичний перезапуск гри
    else:
        stat.append(Statistics(SCORE, LOST, diff_timer, LEVEL))
        finish = False
        SCORE = 0
        LOST = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()

        pygame.time.delay(3000)
        for i in range(1, 6):
            monster = Enemy(IMG_ENEMY, randint(80, WIN_WIDTH - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        TIMER = time.time()
    pygame.time.delay(FPS)


save_statistics(PATH_FILE_STAT)
