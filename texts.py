import pygame
from settings import Settings


class Tap():
    """表示游戏导览的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 导入屏幕和设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/tutorial.png')
        self.rect = self.image.get_rect()

        # 设定位置
        self.rect.x = 0.3 * self.init_settings.screen_width
        self.rect.y = 0.5 * self.init_settings.screen_height

    def blitme(self):
        """显示图形"""
        self.screen.blit(self.image, self.rect)


class Title():
    """表示游戏标题的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 导入屏幕和设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/text_ready.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定位置
        self.rect.x = 0.15 * self.init_settings.screen_width
        self.rect.y = 0.3 * self.init_settings.screen_height

    def blitme(self):
        """显示图形"""
        self.screen.blit(self.image, self.rect)


class Over():
    """表示游戏结束标题的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 导入屏幕和设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/text_game_over.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 设定位置
        self.rect.x = 0.15 * self.init_settings.screen_width
        self.rect.y = 0.35 * self.init_settings.screen_height

    def blitme(self):
        """显示图形"""
        self.screen.blit(self.image, self.rect)
