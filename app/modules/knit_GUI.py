
from modules.model import Model
from modules.components.trace_render import TraceRender
import pygame
import os

from modules.components.node_render import NodeRender

class KnitGUI:
    def __init__(self, model):

        self.__model = model

        os.environ['SDL_VIDEO_WINDOW_POS'] = '100,50'

        self.__screen = None
        self.__bufferScreen = None
        self.__width = None
        self.__height = None

        self.__backgroundColor = (110, 106, 98)
        self.__icon = pygame.image.load("C:/Users/Ethan/Documents/KNIT/app/modules/assets/icon.png")
        self.__font = None

        self.__appRunning = True

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
                pygame.draw.line(self.__bufferScreen, (0, 0, 0), (self.__socketQueue[i].getX(), self.__socketQueue[i].getY()),
                                                                        (self.__socketQueue[i+1].getX(), self.__socketQueue[i+1].getY()), 2)
        else:
            for i in range(0, len(self.__socketQueue), 2):
                if i == len(self.__socketQueue) - 1:
                    break;
                else:
                    pygame.draw.line(self.__bufferScreen, (0, 0, 0), (self.__socketQueue[i].getX(), self.__socketQueue[i].getY()),
                                                                        (self.__socketQueue[i+1].getX(), self.__socketQueue[i+1].getY()), 2)
        print("__all socket pairs reconstructed__")

    def constructNodes(self):
        self.__nodes = []

        for node in self.__model.getNodes():
            nodeRendering = NodeRender(node, node.getX(), node.getY(), 100, 100)
            self.__nodes.append(nodeRendering)
            pygame.draw.rect(self.__bufferScreen, 
                             nodeRendering.getColor(), 
                             nodeRendering.getNodeRender(),
                             border_radius=5,
                             width=3)
            
            node = nodeRendering.getNode()
            nodeIDText = self.__font.render(f"ID: {node.getIdentifier()}", True, (0, 0, 0))
            nodeIDTextRect = nodeIDText.get_rect()
            nodeIDTextRect.topleft = (nodeRendering.getX() + nodeRendering.getWidth() // 10, nodeRendering.getY() + nodeRendering.getHeight() // 10)
            self.__bufferScreen.blit(nodeIDText, nodeIDTextRect)

            nodeFUNCText = self.__font.render(f"FUNC: {node.getFunctionName()}", True, (0, 0, 0))
            nodeFUNCTextRect = nodeFUNCText.get_rect()
            nodeFUNCTextRect.topleft = (nodeRendering.getX() + nodeRendering.getWidth() // 10, nodeIDTextRect.y + nodeIDTextRect.height)
            self.__bufferScreen.blit(nodeFUNCText, nodeFUNCTextRect)

            nodeRendering.addSockets()
            for socket in nodeRendering.getSockets():
                pygame.draw.circle(self.__bufferScreen, socket.getColor(), (socket.getX(), socket.getY()), socket.getRadius())

            for socket in nodeRendering.getSockets():
                for idIndex, queueId in enumerate(self.__socketQueue):
                    if socket.getRenderId() == queueId:
                        self.__socketQueue[idIndex] = socket

        self.renderSocketPairs()

                
        self.__screen.blit(self.__bufferScreen, (0,0))
        pygame.display.update()
            

    def rerenderAll(self, singleNode=None):
        self.__bufferScreen.fill(self.__backgroundColor)
        for nodeRendering in self.__nodes:
            pygame.draw.rect(self.__bufferScreen, 
                    nodeRendering.getColor(), 
                    nodeRendering.getNodeRender(),
                    border_radius=5,
                    width=3)

            node = nodeRendering.getNode()
            nodeIDText = self.__font.render(f"ID: {node.getIdentifier()}", True, (0, 0, 0))
            nodeIDTextRect = nodeIDText.get_rect()
            nodeIDTextRect.topleft = (nodeRendering.getX() + nodeRendering.getWidth() // 10, nodeRendering.getY() + nodeRendering.getHeight() // 10)
            self.__bufferScreen.blit(nodeIDText, nodeIDTextRect)

            nodeFUNCText = self.__font.render(f"FUNC: {node.getFunctionName()}", True, (0, 0, 0))
            nodeFUNCTextRect = nodeFUNCText.get_rect()
            nodeFUNCTextRect.topleft = (nodeRendering.getX() + nodeRendering.getWidth() // 10, nodeIDTextRect.y + nodeIDTextRect.height)
            self.__bufferScreen.blit(nodeFUNCText, nodeFUNCTextRect)

            nodeRendering.updateSockets()
            for socket in nodeRendering.getSockets():
                pygame.draw.circle(self.__bufferScreen, socket.getColor(), (socket.getX(), socket.getY()), socket.getRadius())

            self.renderSocketPairs()
                
        self.__screen.blit(self.__bufferScreen, (0,0))
        pygame.display.update()
        


    def run(self):

        pygame.init()

        self.__font = pygame.font.Font(None, 18)

        self.__screen = pygame.display.set_mode()

        self.__width, self.__height = self.__screen.get_size()
        self.__screen = pygame.display.set_mode((self.__width - 200, self.__height - 200))
        self.__bufferScreen = pygame.Surface((self.__width, self.__height))
        self.__bufferScreen.fill(self.__backgroundColor)

        pygame.display.set_caption('K.N.I.T.')

        self.__screen.fill(self.__backgroundColor)
        pygame.display.set_icon(self.__icon)

        self.constructNodes()

        socketBufferHead = None
        socketBufferTail = None

        offsetX = 0
        offsetY = 0
        targetNode = None
        dragging = False

        while (self.__appRunning):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.__appRunning = False
                    self.__model.saveModel(self.__nodes, self.__socketQueue)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__appRunning = False
                        self.__model.saveModel(self.__nodes, self.__socketQueue)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    node_clicked = False
                    for index, node in enumerate(self.__nodes):
                        if node.getNodeRender().collidepoint(event.pos):
                            dragging = True
                            targetNode = index

                            offsetX = event.pos[0] - node.getX()
                            offsetY = event.pos[1] - node.getY()
                            print("node clicked")
                            node_clicked = False

                        for socket in node.getSockets():
                            if socket.getSocketRender().collidepoint(event.pos):
                                ## if socket already in queue and it is clicked again,
                                ## call on function to remove from queue. If even elem in queue
                                ## remove the socket and the one paired with it in sliding window,
                                ## otherwise just remove that socket.
                                if socket in self.__socketQueue:
                                    self.dequeueSocket(socket)
                                else:
                                    self.__socketQueue.append(socket)
                                
                    self.rerenderAll()


                if event.type == pygame.MOUSEBUTTONUP:
                    dragging = False

                if event.type == pygame.MOUSEMOTION:
                    if dragging:
                        self.__nodes[targetNode].setX(event.pos[0] - offsetX)
                        self.__nodes[targetNode].setY(event.pos[1] - offsetY)
                        #self.__nodes[targetNode].updateSockets()
                        self.rerenderAll()
            # print(len(self.__socketQueue), [str(socket) for socket in self.__socketQueue])  
            #self.enqueueFromReader()
            pygame.display.update()
            #exit()
