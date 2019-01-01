import pygame
from pygame.sprite import Sprite


class PipeDown(Sprite):
    """表示下面柱子的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 继承
        super().__init__()

        # 导入屏幕和设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/pipe_up.png')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.init_settings.screen_width
        self.x = float(self.rect.x)

    def blitme(self, height):
        """显示柱子,height为高度"""
        self.rect.y = height
        self.screen.blit(self.image, self.rect)


class PipeUp(Sprite):
    """表示上面柱子的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 继承
        super().__init__()

        # 导入屏幕和设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/pipe_down.png')
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.x = self.init_settings.screen_width
        self.x = float(self.rect.x)

    def blitme(self, height):
        """显示柱子,height为高度"""
        self.rect.y = height
        self.screen.blit(self.image, self.rect)
