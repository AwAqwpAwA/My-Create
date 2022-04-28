print("函数模块加载完毕")

import pygame
from 设置 import *
from 信息文件 import *
Window = None
时钟 = pygame.time.Clock()

def 帧率():时钟.tick(FPS)

def 初始化():
    global Window
    pygame.init()
    Window = pygame.display.set_mode(Win)
    pygame.display.set_caption(标题)
    icon = pygame.Surface((32,32))
    icon.fill("white")
    pygame.display.set_icon(icon)
    pygame.display.flip()

def 主函数():
    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:quit()