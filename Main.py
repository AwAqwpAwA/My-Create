#主文件

import pygame # 导入 Pygame 模块
from Settings import * # 导入 设置 模块
from Function import * # 导入 函数 模块
from Block import * # 导入 方块 模块

window = pygame.display.set_mode(Win) # 设置 窗口
pygame.display.set_caption(title) # 设置 窗口名
pygame.init()
FPS = pygame.time.Clock() # 创建时钟
Font = pygame.font.SysFont('microsoftyaheiui',20)

HUD = True # 是否显示 HUD

M_x , M_y = 0, 0

while True : # 主循环

    FPS.tick(fps) # 设置帧数

    window.fill((255,255,255)) # 填充背景

    for 事件 in pygame.event.get(): # 获取事件
        if 事件.type == pygame.QUIT : quit() # 退出游戏
        if 事件.type == pygame.MOUSEMOTION : 
            M_x , M_y = 事件.pos
            M_x -= 50
            M_y -= 50
            M_x //= 32
            M_y //= 32
        if 事件.type == pygame.KEYDOWN:
            if 事件.key == pygame.K_h : HUD = Change(HUD)

    Set_texture(铜矿石,48,48)

    if HUD :
        绘制矩形("black",M_x * 32 + 48 , M_y * 32 + 48 ,32,32,1)
        绘制矩形("orange",0,0,Win_h,Win_w,48)

    pygame.display.update() # 刷新
