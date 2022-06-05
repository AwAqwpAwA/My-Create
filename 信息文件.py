from 设置 import * #导入"输出日志函数"

class 信息: #定义信息
    def __init__(self,run,name,size,texture,info):
        def draw(Direction):pass #绘制函数
        self.run = run #运行
        self.name = name #名称
        self.size = size #尺寸
        self.texture = texture #材质
        self.info = info #其他参数
        self.draw = draw() #绘制

log("信息文件加载完毕") #返回日志