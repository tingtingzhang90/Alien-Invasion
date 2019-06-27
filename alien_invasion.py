import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    ai_settings.screen_width = screen.get_rect().width
    ai_settings.screen_height = screen.get_rect().height
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()

    aliens = pygame.sprite.Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
