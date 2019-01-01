import pygame


class Settings():
    """存储设置信息"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.pipe_image = pygame.image.load('resources/sprites/pipe_up.png')
        self.screen_width = 288
        self.screen_height = 512
        self.bg_day = pygame.image.load('resources/sprites/bg_day.png')

        # 初始key_down值
        self.default_key_down = 6

        # 初始fps_count
        self.fps_count = 0

        # 柱子各项参数
        self.pipe_speed_factor = 5
        self.pipe_height = self.pipe_image.get_height()
        self.pipe_width = self.pipe_image.get_width()
        self.move_distance = self.screen_width * 4 // 3 + self.pipe_image.get_width()
