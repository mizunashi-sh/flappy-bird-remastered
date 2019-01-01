import pygame
from pygame.sprite import Sprite


class Ground(Sprite):
    """表示地面的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 继承
        super(Ground, self).__init__()

        # 导入屏幕和初始设定
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取其rect
        self.image = pygame.image.load('resources/sprites/land.png')
        self.rect = self.image.get_rect()
        self.fps = self.init_settings.fps_count

        # 初始位置
        self.rect.x = 0
        self.rect.y = 0.8 * self.init_settings.screen_height

    def blitme(self):
        # 更新位置
        self.fps += 1
        self.rect.x = -1 * ((self.fps * 4) %
                            (self.image.get_width() - self.init_settings.screen_width))

        # 显示地面
        self.screen.blit(self.image, self.rect)
