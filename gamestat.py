import pygame


class Score():
    """表示分数的类"""

    def __init__(self, init_settings, screen):
        """导入屏幕和设定"""
        self.screen = screen
        self.init_settings = init_settings

        """导入图片资源"""
        self.images = [
            pygame.image.load('resources/sprites/font_048.png'),
            pygame.image.load('resources/sprites/font_049.png'),
            pygame.image.load('resources/sprites/font_050.png'),
            pygame.image.load('resources/sprites/font_051.png'),
            pygame.image.load('resources/sprites/font_052.png'),
            pygame.image.load('resources/sprites/font_053.png'),
            pygame.image.load('resources/sprites/font_054.png'),
            pygame.image.load('resources/sprites/font_055.png'),
            pygame.image.load('resources/sprites/font_056.png'),
            pygame.image.load('resources/sprites/font_057.png')
        ]

    def showScore(self, score):
        """显示分数"""
        # 计算图片位置
        scoreList = [int(i) for i in list(str(score))]
        total_width = 0

        for digit in scoreList:
            total_width += self.images[digit].get_width()

        pos_x = (self.init_settings.screen_width - total_width) // 2
        pos_y = int(0.2 * self.init_settings.screen_height)

        # 显示分数
        for digit in scoreList:
            self.screen.blit(self.images[digit], (pos_x, pos_y))
            pos_x += self.images[digit].get_width()
