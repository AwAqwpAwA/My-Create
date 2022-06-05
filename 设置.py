
from 函数 import log #导入"输出日志函数"

Mods = [] #模组列表

HUD_h , HUD_w = 42 , 42 #设置HUD长宽
HUD = HUD_h , HUD_w #设置HUD长宽
Win_h , Win_w = 32 * 24 + HUD_h , 32 * 24 + HUD_w #设置窗口长宽
Win = Win_h , Win_w #设置窗口长宽

标题 = "My Create" #设置标题
FPS = 60 #设置帧数

log("设置文件加载完毕")# 返回日志