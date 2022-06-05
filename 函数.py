
import os #导入模块
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "Don't bb!!!" #禁止导入Pygame时瞎BB

def 帧率():时钟.tick(FPS) #设置时钟

def 初始化(): #初始化函数
    global Window #创建窗口
    pygame.init() #Pygame初始化
    Window = pygame.display.set_mode(Win) #设置窗口大小
    pygame.display.set_caption(标题) #设置标题
    icon = pygame.Surface((32,32)) #设置图标对象
    icon.fill("white") #填充图标
    pygame.display.set_icon(icon) #设置图标
    pygame.display.flip() #第一次刷新

def 主函数(): #主函数
    global 退出 #引入全局变量
    for 事件 in pygame.event.get(): #监测事件
        if 事件.type == pygame.QUIT:退出()#退出

def log(*str): #日志函数
    import time #导入时间模块
    today = time.localtime(time.time()) #得到时间信息
    print(f"[{today.tm_year}/{today.tm_mon}/{today.tm_mday}][{today.tm_hour}:{today.tm_min}:{today.tm_sec}]",end="") #输出时间
    for i in str: #循环
        print(i,end="") #输出日志内容
    print("") #换行

def 加载模组(): #加载模组函数
    global Mods #引入全局变量
    import sys,os #导入模块
    try: #尝试
        os.mkdir("mods") #创建文件夹
    except:pass #否则直接跳过
    sys.path.append("mods") #设置模组路径
    List = os.listdir("mods") #获得文件夹下所有文件
    for i in List: #循环
        try: #尝试
            if i[-3:] == ".py": #检测后缀是否为".py"
                Mods.append(i[:-3]) #加入模组列表
                log(f"加载模组[{i[:-3]}]") #输出日志
                __import__(i[:-3]) #导入改模块
        except:pass #失败就直接跳过
    if not len(Mods):log("没有任何模组加载") #输出日志
    else:
        log(f"共加载{len(Mods)}个模组")

def 退出(): #退出函数
    log("游戏已退出")
    exit() #退出

import pygame #导入Pygame
from 信息文件 import * #导入信息文件

Window = None #设置变量
时钟 = pygame.time.Clock() #创建时钟

log("函数模块加载完毕") #输出日志