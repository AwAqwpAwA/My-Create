#函数

def Change(Bool):return not Bool

def 绘制矩形(颜色,X,Y,H,W,线宽 = 0): # 绘制矩形函数
    import pygame # 导入 Pygame 模块
    from Main import window # 导入 窗口参数
    pygame.draw.rect(window,颜色,(X,Y,H,W),线宽) # 绘制矩形

def Set_texture(T,x,y) :
    Return = []
    for i in T.texture:
        for I in range(0,i[1]):Return.append(i[0])

    Print = []
    for i in range(0,int(len(Return)/16*T.size[0])+1):
        Print.append(Return[16*T.size[0]*i:16*(T.size[0]+i)])
    
    for i in range(0,len(Print)):
        for I in range(0,len(Print[i])):
            if Print[i][I] != "N" :
                绘制矩形(Print[i][I],I*2+x,i*2+y,2,2)
