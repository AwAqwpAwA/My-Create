#函数

def Change(Bool):return not Bool

def 绘制矩形(颜色,X,Y,H,W,线宽 = 0): # 绘制矩形函数
    import pygame # 导入 Pygame 模块
    from Main import window # 导入 窗口参数
    pygame.draw.rect(window,颜色,(X,Y,H,W),线宽) # 绘制矩形

def Read_texture(texture) :
    Return = []
    for i in range(0,len(texture)):
        for ii in range(0,texture[i][1]):
            Return.append(texture[i][0])
    return Return

def Draw_block(texture):pass