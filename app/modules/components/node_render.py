import pygame
from modules.components.socket_render import SocketRender

class NodeRender:
    __renderID = 1
    def __init__(self, node, coorX, coorY, globalWidth=65, globalHeight=65):
        self.__renderID = NodeRender.__renderID
        NodeRender.__renderID += 1

        self.__node = node

        self.__x = coorX
        self.__y = coorY
        self.__globalWidth = globalWidth
        self.__globalHeight = globalHeight

        self.__color = (52, 174, 235)

        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

        ## for node connections and renderings
        self.__sockets = []
        self.__traces = []

        ## data calculated on first go around of adding sockets
        ## used later in updateSockets()
        self.__inputIncrement = 0
        self.__outputIncrement = 0
        self.__numberInputs = 0
        self.__numberOutputs = 0

    def getNode(self):
        return self.__node
    
    def setNode(self, node):
        self.__node = node

    def getNodeRender(self):
        return self.__nodeRender
    
    def setX(self, val):
        self.__x = val
        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

    def getX(self):
        return self.__x
    
    def setY(self, val):
        self.__y = val
        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

    def getY(self):
        return self.__y
    
    def getHeight(self):
        return self.__globalHeight
    
    def getWidth(self):
        return self.__globalWidth
    
    def setHeight(self, height):
        self.__globalHeight = height
        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

    def setWidth(self, width):
        self.__globalWidth = width
        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

    def setColor(self, value):
        self.__color = value
        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

    def getColor(self):
        return self.__color
    
    def getRenderId(self):
        return self.__renderID
    
    def resetSockets(self):
        self.__sockets = []
    
    def getSockets(self):
        return self.__sockets
    
    def addSockets(self):
        self.__numberInputs = len(self.__node.getInputIdentifiers())
        self.__numberOutputs = len(self.__node.getOutputIdentifiers())
        if self.__numberInputs != 0:
            self.__inputIncrement = self.__globalHeight // (self.__numberInputs + 1)
        if self.__numberOutputs != 0:
            self.__outputIncrement = self.__globalHeight // (self.__numberOutputs + 1)

        if self.__numberInputs != 0 and self.__node.getInputIdentifiers()[0] != -1:
            x = self.__x
            y = self.__y
            for i in range(self.__numberInputs):
                y += self.__inputIncrement
                newSocketRender = SocketRender(self.__node, x, y, True)
                self.__sockets.append(newSocketRender)

        if self.__numberOutputs != 0 and self.__node.getOutputIdentifiers()[0] != -2:
            x = self.__x + self.__globalWidth
            y = self.__y
            for i in range(self.__numberOutputs):
                y += self.__outputIncrement
                newSocketRender = SocketRender(self.__node, x, y, False)
                self.__sockets.append(newSocketRender)

    def updateSockets(self):
        scopedInputX = self.__x
        scopedInputY = self.__y
        scopedOutputX = self.__x + self.__globalWidth
        scopedOutputY = self.__y
        # print("new call")
        for socket in self.__sockets:
            if socket.isInput():
                x = scopedInputX
                scopedInputY += self.__inputIncrement
                y = scopedInputY
                socket.setX(x)
                socket.setY(y)
            else:
                x = scopedOutputX 
                scopedOutputY += self.__outputIncrement
                y = scopedOutputY
                socket.setX(x)
                socket.setY(y)

    def getTraces(self):
        return self.__traces
    
    def addTrace(self, trace):
        self.__traces.append(trace)