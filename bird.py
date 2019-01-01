import pygame
from itertools import cycle
from pygame.sprite import Sprite


class Bird(Sprite):
    """用来表示鸟的类"""

    def __init__(self, init_settings, screen):
        """初始化类"""
        # 继承
        super(Bird, self).__init__()

        # 导入背景和游戏默认设定
        self.screen = screen
        self.init_settings = init_settings

        # 图片资源
        self.images = [
            pygame.image.load('resources/sprites/bird0_0.png'),
            pygame.image.load('resources/sprites/bird0_1.png'),
            pygame.image.load('resources/sprites/bird0_2.png'),
        ]
        self.wing_sound = pygame.mixer.Sound('resources/sounds/sfx_wing.wav')

        # 帧数统计与迭代器，主要用来控制小鸟翅膀的抖动
        self.fps = self.init_settings.fps_count
        self.wing_position_iter = cycle([0, 1, 2])
        self.wing_position = 0
        self.bird_shake = 0
        self.bird_shake_iter = cycle(
            [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -3, -2, -1])

        # 重力加速度值,默认下落速度和函数调用次数
        self.gravity = 1
        self.down_speed = 0
        self.call_count = 0

        # 用来存储当前小鸟的图像及其rect,默认值为0
        self.image = 0
        self.rect = 0
        # 临时存储小鸟位置
        self.pos_x = 0
        self.pos_y = 0

    def blitme(self, stat, key_down=0):
        """在屏幕上展示抖动的小鸟"""
        # 使小鸟的翅膀抖动起来
        self.fps += 1
        if self.fps % 5 == 0:
            self.wing_position = next(self.wing_position_iter)
        self.bird_shake = next(self.bird_shake_iter)
        image = self.images[self.wing_position]

        # 当前小鸟的图形和位置
        self.image = image
        self.rect = image.get_rect()

        # 若函数未被调用，初始化当前位置为默认值
        # 若函数已经被调用，则更新位置
        if not self.call_count:
            self.rect.x = int(0.2 * self.init_settings.screen_width)
            self.rect.y = int(
                0.5 * self.init_settings.screen_height) + self.bird_shake
            self.pos_x = self.rect.x
            self.pos_y = self.rect.y
        else:
            self.rect.x = self.pos_x
            self.rect.y = self.pos_y

        # 当stat为1,即游戏正在进行时,用键盘控制小鸟
        if stat == 1:
            # 更新函数调用次数为非0
            self.call_count = 1
            # 如果按下空格键,即key_down非0,则向上升,并播放音效
            # 反之下降
            if key_down:
                self.rect.y -= 10
                self.rect.y = max(0, self.rect.y)
                self.pos_y = self.rect.y
                self.down_speed = 0
                self.wing_sound.play()
            else:
                self.down_speed += self.gravity
                self.rect.y += self.down_speed
                self.rect.y = min(
                    self.init_settings.screen_height, self.rect.y)
                self.pos_y = self.rect.y

        # 在屏幕上显示小鸟
        self.screen.blit(image, self.rect)

    def fall(self, ground):
        """使小鸟撞地或撞柱子后下落"""
        # 更新位置信息
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        # 下落
        self.down_speed += self.gravity
        self.rect.y += self.down_speed
        # 若小鸟已经碰到地面，则不再下落
        if self.rect.bottom > ground.rect.top:
            self.rect.bottom = ground.rect.top
        self.pos_y = self.rect.y

        # 显示小鸟
        self.screen.blit(self.image, self.rect)
