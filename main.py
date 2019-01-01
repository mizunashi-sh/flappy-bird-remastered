import sys
import random
import pygame
import texts
from bird import Bird
from gamestat import Score
from ground import Ground
from pipes import PipeUp, PipeDown
from settings import Settings
from buttom import Buttom


def run_game():
    # 初始化
    pygame.init()
    # 导入设定
    init_settings = Settings()

    # 分数,按键记录,游戏状态初始值
    current_score = 0
    key_down = 0
    # game_stat的0表示初始界面,1表示游戏正在进行,2表示游戏结束
    game_stat = 0

    # 声音资源
    hit_sound = pygame.mixer.Sound('resources/sounds/sfx_hit.wav')
    die_sound = pygame.mixer.Sound('resources/sounds/sfx_die.wav')
    point_sound = pygame.mixer.Sound('resources/sounds/sfx_point.wav')

    # 设定窗口大小
    screen = pygame.display.set_mode(
        (init_settings.screen_width, init_settings.screen_height))
    # 游戏中各种类的实例
    my_ground = Ground(init_settings, screen)
    my_bird = Bird(init_settings, screen)
    pipedown1 = PipeDown(init_settings, screen)
    pipeup1 = PipeUp(init_settings, screen)
    pipedown2 = PipeDown(init_settings, screen)
    pipeup2 = PipeUp(init_settings, screen)

    # 柱子的高度,间隙和位置的初始信息
    down_position1 = 0
    gap1 = 150
    down_position2 = 0
    gap2 = 150
    up_position2 = 0
    pipeup1.rect.x = init_settings.screen_width
    pipedown1.rect.x = init_settings.screen_width
    pipeup2.rect.x = init_settings.screen_width
    pipedown2.rect.x = init_settings.screen_width

    # 游戏中提示文本与按钮的实例
    tap = texts.Tap(init_settings, screen)
    score = Score(init_settings, screen)
    title = texts.Title(init_settings, screen)
    over_text = texts.Over(init_settings, screen)
    play_buttom = Buttom(init_settings, screen)

    # 控制动画速度
    FPS = pygame.time.Clock()
    # 设置窗口标题
    pygame.display.set_caption('Flappy Bird')

    while True:

        for event in pygame.event.get():
            # 处理事件
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # 当空格键按下
                if game_stat == 0:
                    # 从初始界面切换到进行界面
                    game_stat = 1
                elif game_stat == 1:
                    # 将key_down值设为初始
                    key_down = init_settings.default_key_down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 当鼠标按下,获取光标位置
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_buttom.rect.collidepoint(mouse_x, mouse_y):
                    # 若点击开始游戏按钮，则将状态切换至开始动画,并初始化相关变量和实例
                    game_stat = 0
                    current_score = 0
                    key_down = 0

                    pipeup1.rect.x = init_settings.screen_width
                    pipedown1.rect.x = init_settings.screen_width
                    pipeup2.rect.x = init_settings.screen_width
                    pipedown2.rect.x = init_settings.screen_width

                    my_bird = Bird(init_settings, screen)

        if game_stat == 0:
            # 显示背景和各种实例
            screen.blit(init_settings.bg_day, (0, 0))
            my_bird.blitme(0)
            my_ground.blitme()
            tap.blitme()
            title.blitme()
            score.showScore(0)
        elif game_stat == 1:
            # 导入用于动画的相关变量
            move_distance = init_settings.move_distance
            fps_count = init_settings.fps_count

            # 显示背景
            screen.blit(init_settings.bg_day, (0, 0))

            # 画面中同时最多生成两个柱子
            # 用随机数生成第一对柱子的高度和空隙大小
            fps_count += 1
            if pipeup1.rect.x == init_settings.screen_width:
                down_position1 = random.randrange(int(
                    0.3 * init_settings.screen_height), int(0.7 * init_settings.screen_height), 10)
                gap1 = random.randrange(100, 151, 10)
            up_position1 = down_position1 - gap1 - init_settings.pipe_height
            # 让第一对柱子动起来
            pipeup1.rect.x -= init_settings.pipe_speed_factor
            pipedown1.rect.x -= init_settings.pipe_speed_factor
            pipedown1.blitme(down_position1)
            pipeup1.blitme(up_position1)

            # 当第一对柱子运动到指定位置,用随机数生成第二对柱子的高度和空隙大小
            if pipeup1.rect.x == 143:
                if pipeup2.rect.x == init_settings.screen_width:
                    down_position2 = random.randrange(int(
                        0.3 * init_settings.screen_height), int(0.7 * init_settings.screen_height), 10)
                    gap2 = random.randrange(100, 151, 10)
                up_position2 = down_position2 - gap2 - init_settings.pipe_height
            # 第二对柱子动起来
            if (pipeup1.rect.x < 0.5 *
                init_settings.screen_width and pipeup1.rect.x > -
                1 *
                init_settings.pipe_width) or (pipeup2.rect.x < 0.5 *
                                              init_settings.screen_width and pipeup2.rect.x > -
                                              1 *
                                              init_settings.pipe_width):
                pipeup2.rect.x -= init_settings.pipe_speed_factor
                pipedown2.rect.x -= init_settings.pipe_speed_factor
                pipedown2.blitme(down_position2)
                pipeup2.blitme(up_position2)

            # 碰撞检测
            # 若小鸟碰到柱子或者地面,则播放死亡音效,将游戏状态设为2,进入游戏结束画面
            # 使用了pygame中的像素遮罩检测,更加精确
            if pygame.sprite.collide_mask(
                my_bird, pipeup1) or pygame.sprite.collide_mask(
                my_bird, pipeup2) or pygame.sprite.collide_mask(
                my_bird, pipedown1) or pygame.sprite.collide_mask(
                my_bird, pipedown2) or pygame.sprite.collide_mask(
                    my_bird, my_ground):
                hit_sound.play()
                die_sound.play()
                game_stat = 2
                continue

            # 计分,当小鸟完全通过一对柱子时加1分,并播放加分音效
            if (my_bird.rect.x > pipeup1.rect.left and my_bird.rect.x < pipeup1.rect.right) or (
                    my_bird.rect.x > pipeup2.rect.left and my_bird.rect.x < pipeup2.rect.right):
                current_score += 1
                if not (current_score + 10) % 10:
                    point_sound.play()

            # 当柱子到达窗口最左侧时,刷新柱子位置,使其从最右侧开始运动
            if pipeup1.rect.x <= -1 * init_settings.pipe_width:
                pipeup1.rect.x = init_settings.screen_width
            if pipedown1.rect.x <= -1 * init_settings.pipe_width:
                pipedown1.rect.x = init_settings.screen_width
            if pipeup2.rect.x <= -1 * init_settings.pipe_width:
                pipeup2.rect.x = init_settings.screen_width
            if pipedown2.rect.x <= -1 * init_settings.pipe_width:
                pipedown2.rect.x = init_settings.screen_width

            # 显示小鸟
            my_bird.blitme(1, key_down)
            # 显示地面
            my_ground.blitme()
            # 显示分数
            score.showScore(current_score // 10)

            # 更新key_down值
            if key_down:
                key_down -= 1
        elif game_stat == 2:
            # 显示背景
            screen.blit(init_settings.bg_day, (0, 0))
            # 在原位置显示柱子
            pipedown1.blitme(down_position1)
            pipeup1.blitme(up_position1)
            pipedown2.blitme(down_position2)
            pipeup2.blitme(up_position2)
            # 小鸟下落至地面
            my_bird.fall(my_ground)
            # 显示地面
            my_ground.blitme()
            # 显示游戏结束文本
            over_text.blitme()
            # 显示分数
            score.showScore(current_score // 10)
            # 显示开始按钮
            play_buttom.blitme()

        # 更新画面
        pygame.display.update()
        FPS.tick(30)


run_game()
