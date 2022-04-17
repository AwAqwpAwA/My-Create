#类

class Info :
    def __init__( self, type , size , texture ):
        self.type = type
        self.size = size
        self.texture = texture

class Map :
    def __init__( self , name , block ,liquid ) : 
        self.name = name
        self.block = block
        self.Liquid = liquid