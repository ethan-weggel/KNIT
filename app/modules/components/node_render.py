import pygame
from modules.components.socket_render import SocketRender

class NodeRender:
    __renderID = 1
    def __init__(self, node, coorX, coorY, globalWidth=50, globalHeight=50):
        self.__renderID = NodeRender.__renderID
        NodeRender.__renderID += 1

        self.__node = node

        self.__x = coorX
        self.__y = coorY
        self.__globalWidth = globalWidth
        self.__globalHeight = globalHeight

        self.__color = (52, 174, 235)

        self.__nodeRender = pygame.Rect(self.__x, self.__y, self.__globalWidth, self.__globalHeight)

        self.__sockets = []
        self.__traces = []

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
        numberInputSockets = len(self.__node.getInputIdentifiers())
        numberOutputSockets = len(self.__node.getOutputIdentifiers())
        if numberInputSockets != 0:
            inputIncrement = self.__globalHeight // (numberInputSockets + 1)
        if numberOutputSockets != 0:
            outIncrement = self.__globalHeight // (numberOutputSockets + 1)

        if numberInputSockets != 0:
            x = self.__x
            y = self.__y
            for i in range(numberInputSockets):
                y += inputIncrement
                newSocketRender = SocketRender(self.__node, x, y)
                self.__sockets.append(newSocketRender)

        if numberOutputSockets != 0:
            x = self.__x + self.__globalWidth
            y = self.__y
            for i in range(numberOutputSockets):
                y += outIncrement
                newSocketRender = SocketRender(self.__node, x, y)
                self.__sockets.append(newSocketRender)
            
    def getTraces(self):
        return self.__traces
    
    def addTrace(self, trace):
        self.__traces.append(trace)