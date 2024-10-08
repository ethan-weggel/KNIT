# from modules.model import Model
# from modules.components.trace_render import TraceRender
# from modules.components.button import Button
# from modules.node import Node
import pygame
import os
import sys

# from modules.components.node_render import NodeRender


modelPath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\model.py")
nodeRenderPath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\components\\node_render.py")
nodePath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\node.py")
tracePath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\components\\trace_render.py")
socketRenderPath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\components\\socket_render.py")
buttonPath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\components\\button.py")
sys.path.insert(0, modelPath)
sys.path.insert(0, nodeRenderPath)
sys.path.insert(0, socketRenderPath)
sys.path.insert(0, nodePath)
sys.path.insert(0, tracePath)
sys.path.insert(0, buttonPath)

from model import Model # type: ignore
from node_render import NodeRender # type: ignore
from node import Node # type: ignore
from trace_render import TraceRender # type: ignore
from socket_render import SocketRender # type: ignore
from button import Button # type: ignore

class HeadlessHorseman:

    def __init__(self, model):

        self.__model = model

        self.__screen = None
        self.__bufferScreen = None
        self.__width = None
        self.__height = None

        self.__nodes = None

        self.__socketQueue = self.__model.getSocketQueue()

    def getWidth(self):
        if self.__width != None:
            return self.__width
        
    def getHeight(self):
        if self.__height != None:
            return self.__height
        
    def getScreenObj(self):
        if self.__screen != None:
            return self.__screen

        
    def dequeueSocket(self, socket):
        _isEven = len(self.__socketQueue) % 2 == 0
        if _isEven:
            for i in range(0, len(self.__socketQueue), 2):
                socketPair = (self.__socketQueue[i], self.__socketQueue[i+1])
                if socket in socketPair:
                    socketPair[0].getNode().unplugOutput(node=socketPair[1].getNode())
                    socketPair[1].getNode().unplugInput(node=socketPair[0].getNode())
                    self.__socketQueue.remove(socketPair[0])
                    self.__socketQueue.remove(socketPair[1])
                    return
        else:
            for i in range(0, len(self.__socketQueue), 2):
                if socket == self.__socketQueue[i]:
                    self.__socketQueue.remove(socket)
                    return
                    
        print("__socket queue refactored__")
        
    def renderSocketPairs(self):

        _isEven = len(self.__socketQueue) % 2 == 0

        if _isEven:
            for i in range(0, len(self.__socketQueue), 2):
                self.__socketQueue[i].getNode().resetSockets()
                self.__socketQueue[i+1].getNode().resetSockets()

        if _isEven:
            for i in range(0, len(self.__socketQueue), 2):
                self.__socketQueue[i].getNode().plugOutput(self.__socketQueue[i+1].getNode())
                self.__socketQueue[i+1].getNode().plugInput(self.__socketQueue[i].getNode())
        else:
            for i in range(0, len(self.__socketQueue), 2):
                if i == len(self.__socketQueue) - 1:
                    break;
                else:
                    self.__socketQueue[i].getNode().plugOutput(self.__socketQueue[i+1].getNode())
                    self.__socketQueue[i+1].getNode().plugInput(self.__socketQueue[i].getNode())

    def constructNodes(self):
        self.__nodes = []

        for node in self.__model.getNodes():
            nodeRendering = NodeRender(node, node.getX(), node.getY(), 125, 125)
            self.__nodes.append(nodeRendering)
            
            node = nodeRendering.getNode()

            nodeRendering.addSockets()

            for socket in nodeRendering.getSockets():
                for idIndex, queueId in enumerate(self.__socketQueue):
                    if socket.getRenderId() == queueId:
                        self.__socketQueue[idIndex] = socket

        self.renderSocketPairs()
            

    def rerenderAll(self, singleNode=None):
        for nodeRendering in self.__nodes:
            node = nodeRendering.getNode()
            nodeRendering.updateSockets()
            self.renderSocketPairs()

        self.renderButtons()
                
        self.__screen.blit(self.__bufferScreen, (0,0))
        pygame.display.update()
        
    def runButtonFunction(self):
        print("__executing workflow__")
        self.__model.executeWorkflow()

    def run(self):

        self.constructNodes()

        self.__model.executeWorkflow()