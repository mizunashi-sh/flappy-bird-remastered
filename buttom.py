import pygame


class Buttom():
    """表示按键的类"""

    def __init__(self, init_settings, screen):
        """初始化"""
        # 导入屏幕和默认设置
        self.screen = screen
        self.init_settings = init_settings

        # 导入图片资源,获取rect
        self.image = pygame.image.load('resources/sprites/button_play.png')
        self.rect = self.image.get_rect()

        # 设定位置
        self.rect.x = 0.3 * self.init_settings.screen_width
        self.rect.y = 0.5 * self.init_settings.screen_height

    def blitme(self):
        """显示按键"""
        self.screen.blit(self.image, self.rect)
