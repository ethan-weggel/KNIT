import pygame

class SocketRender:
    __renderID = 1
    def __init__(self, node, x, y, radius=5, color=(245, 173, 66)):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__color = color

        self.__node = node

        self.__boundingRect = pygame.Rect(self.__x - self.__radius, self.__y - self.__radius,
                                          self.__radius * 2, self.__radius * 2)
        
        self.__isOccupied = False
        self.__trace = None

        self.__id = SocketRender.__renderID
        SocketRender.__renderID += 1

    def __str__(self):
        return f"SOCKET: {self.__id}"

    def getRenderId(self):
        return self.__id

    def setX(self, value):
        self.__x = value
        self.__boundingRect = pygame.Rect(self.__x - self.__radius, self.__y - self.__radius,
                                          self.__radius * 2, self.__radius * 2)
        if self.__trace != None:
            self.__trace.replaceSocket(self)

    def getX(self):
        return self.__x

    def setY(self, value):
        self.__y = value
        self.__boundingRect = pygame.Rect(self.__x - self.__radius, self.__y - self.__radius,
                                          self.__radius * 2, self.__radius * 2)
        if self.__trace != None:
            self.__trace.replaceSocket(self)

    def getY(self):
        return self.__y
    
    def setRadius(self, value):
        self.__radius = value
        self.__boundingRect = pygame.Rect(self.__x - self.__radius, self.__y - self.__radius,
                                          self.__radius * 2, self.__radius * 2)
        if self.__trace != None:
            self.__trace.replaceSocket(self)

    def getRadius(self):
        return self.__radius
    
    def setColor(self, value):
        self.__color = value

    def getColor(self):
        return self.__color
    
    def getNode(self):
        return self.__node
    
    def setNode(self, node):
        self.__node = node

    def getSocketRender(self):
        return self.__boundingRect
    
    def getIsOccupied(self):
        return self.__isOccupied
    
    def setIsOccupied(self, value):
        self.__isOccupied = value

    def toggleIsOccupied(self):
        if self.__isOccupied:
            self.__isOccupied = False
        else:
            self.__isOccupied = True

    def setTrace(self, trace):
        self.__trace = trace

    def getTrace(self):
        return self.__trace
    
    def removeTrace(self):
        self.__trace = None

    
    


