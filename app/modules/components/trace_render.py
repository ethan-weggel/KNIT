import pygame

class TraceRender:
    __id = 1
    def __init__(self):
        self.__id = TraceRender.__id
        TraceRender.__id += 1

        self.__sockets = []

    def getSocketXOne(self):
        return self.__sockets[0].getX()
    
    def getSocketYOne(self):
        return self.__sockets[0].getY()
    
    def getSocketXTwo(self):
        return self.__sockets[1].getX()
    
    def getSocketYTwo(self):
        return self.__sockets[1].getY()
    
    def addSocket(self, socket):
        self.__sockets.append(socket)

    def getSockets(self):
        return self.__sockets

    def getRenderId(self):
        return self.__id
    
    def replaceSocket(self, index, socket):
        # for index, currentSocket in enumerate(self.__sockets):
        #     if currentSocket.getRenderId() == socket.getRenderId():
        #         self.__sockets[index] = socket
        self.__sockets[index] = socket