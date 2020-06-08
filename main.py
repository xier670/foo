import pygame                #导入pygame模块
from pygame.locals import *  #导入pygame库中的一些常量
from sys import exit         #导入sys库中的exit函数
import random
import codecs

#设置游戏屏幕大小
SCREEN_WIDTH=480
SCREEN_HEIGHT=800

#初始化pygame
pygame.init()
#设置游戏界面大小
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#设置游戏界面标题
pygame.display.set_caption("彩图版飞机大战")
#设置游戏界面图标位于界面标题前的
picture=pygame.image.load('resources/image/picture.ico').convert_alpha()
pygame.display.set_icon(picture)
#设置背景图
background=pygame.image.load("resources/image/background.png").convert_alpha()



#子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        # 调用父类的初始化方法初始化Sprite的属性
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        self.rect=self.image.get_rect()
        self.rect.midbottom=init_pos
        self.speed=10

    def move(self):
        self.rect.top -= self.speed

#敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_down_imgs,init_pos):
        # 调用父类的初始化方法初始化sprite的属性
        pygame.sprite.Sprite.__init__(self)
        self.image=enemy_img
        self.rect=self.image.get_rect
        self.rect.topleft=init_pos
        self.down_imgs=enemy_down_imgs
        self.speed=2
        self.down_index=0

    #敌机移动，边界判断及删除在游戏主循环里处理
    def move(self):
        self.rect.top +=self.speed


#玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self,player_rect,init_pos):
        #调用父类的初始化方法初始化sprite的属性
        pygame.sprite.Sprite.__init__(self)
        self.image=[] #用来存储玩家飞机图片的列表
        for i in range(len(player_rect)):
            self.image.append(player_rect[i].convert_alpha())

        self.rect=player_rect[0].get_rect()
        self.rect.topleft=init_pos
        self.speed=8
        self.bullets=pygame.sprite.Group()
        self.img_index=0
        self.is_hit=False

    #发射子弹
    def shoot(self,bullet_img):
        bullet=Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)

    #向上移动，需要判断边界
    def moveUp(self):
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top-=self.speed

    #向下移动，需要判断边界
    def moveDown(self):
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top+=self.speed

    #向左移动，需要判断边界
    def moveLeft(self):
        if self.rect.left <=0:
            self.rect.left=0
        else:
            self.rect.left-=self.speed

    #向右移动，需要判断边界
    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left+=self.speed


def startGame():
    #游戏循环帧率
    clock=pygame.time.Clock()
    #判断游戏退出循环参数
    running=True
    #游戏主循环
    while running:
        #绘制背景
        screen.fill(0)
        screen.blit(background,(0,0))
        #控制游戏最大帧率60
        clock.tick(60)
        #更新屏幕
        pygame.display.update()
        #处理游戏退出
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
startGame()
