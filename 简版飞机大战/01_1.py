import math
import pygame
import random


# 初始化界面
pygame.init()
screen = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("feiji")
icon = pygame.image.load("img/feiji.jpg")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("img/bg.png")

# 添加音效
pygame.mixer.music.load("imx/honglianhua.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# 添加击中音效
# 子弹击中
bao_sound = pygame.mixer.Sound("imx/enemy1_down.wav")
# 飞机坠毁
boo_sound = pygame.mixer.Sound("imx/me_down.wav")

# 添加分数
score = 0
# font = pygame.font.Font("freesansbold.ttf", 32)
# 使用中文字体的方法
font = pygame.font.SysFont("simsunnsimsun", 32)  # 宋体

# 游戏结束
is_over = False
font_ = pygame.font.SysFont("simsunnsimsun", 64)


def check_is_over():
    if is_over:
        text = "游戏结束"
        render = font_.render(text, True, (255, 0, 0))
        screen.blit(render, (250, 400))


def show_score():
    text = f"分数: {score}"
    score_render = font.render(text, True, (255, 255, 255))
    screen.blit(score_render, (10, 10))


# 飞机
class Plane:
    def __init__(self):
        self.img = pygame.image.load("img/feiji_2.png")
        self.x = 400
        self.y = 800
        self.step_ud = 0
        self.step_lr = 0

    # 撞到飞机
    def hit_fly(self):
        global is_over
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                boo_sound.play()
                is_over = True
                enemies.clear()


player = Plane()
e_li = []


# 敌机
class Enemy:
    # 添加敌人

    def __init__(self):
        self.img = pygame.image.load("img/enemy.png")
        self.step = random.randint(2, 4)
        self.x = random.randint(20, 780)
        self.y = random.randint(-50, 10)

    def reset(self):
        self.x = random.randint(20, 780)
        self.y = random.randint(-50, 10)

    def e_mov(self):
        if self.x > 1000:
            enemies.remove(self)


# 子弹
class Bullet:
    def __init__(self):
        self.img = pygame.image.load("img/bullet.png")
        self.x = player.x + 35
        self.y = player.y + 10
        self.step = 12

    # 击中
    def hit(self):
        global score
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                bao_sound.play()
                bullets.remove(self)
                e.reset()
                score += 10


# 计算两点直接的距离，
def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)


bullets = []  # 保存现有子弹
enemies = []  # 敌机


# 敌机生成
def generate():
    for i in range(12):
        enemies.append(Enemy())

generate()

# 显示敌机
def show_enemy():
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.y += e.step


# 显示并移动子弹
def show_bullet():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()  # 判断是否击中
        b.y -= b.step
        # 如果子弹出来边界就删除这个 子弹
        if b.y < 0:
            bullets.remove(b)


# 键盘事件和返回

# 移动飞机
def process_events():
    global running
    player.hit_fly()  # 是否撞击
    for event in pygame.event.get():  # 返回事件
        if event.type == pygame.QUIT:  # 退出
            running = False
        # 上下移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.step_ud += 4
            elif event.key == pygame.K_DOWN:
                player.step_ud -= 4
                # 左右移动
            elif event.key == pygame.K_LEFT:
                player.step_lr += 4
            elif event.key == pygame.K_RIGHT:
                player.step_lr -= 4

            # 按下空格发射子弹
            elif event.key == pygame.K_SPACE:
                b = Bullet()
                bullets.append(b)

        if event.type == pygame.KEYUP:
            player.step_ud = 0
            player.step_lr = 0

    screen.blit(player.img, (player.x, player.y))
    player.y -= player.step_ud
    player.x -= player.step_lr


# 防止飞机出界
def boundary():
    if player.y < 0:
        player.y = 0
    if player.y > 900:
        player.y = 900

    if player.x < 0:
        player.x = 0
    if player.x > 720:
        player.x = 720


# 游戏主循环
if __name__ == '__main__':
    running = True
    while running:
        screen.blit(bgImg, (0, 0))  # pygame 的坐标从左上角开开始
        show_score()  # 显示分数
        process_events()  # 控制飞机
        boundary()  # 防止飞机出界

        show_enemy()  # 显示敌人
        show_bullet()  # 显示子弹
        check_is_over()  # 显示游戏结束
        pygame.display.update()
