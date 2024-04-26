import pygame
from node_render import NodeRender

class Button(NodeRender):
    def __init__(self, x, y, width, height, color=(0,0,0), text="BUTTON"):
        super().__init__(x, y, globalWidth=width, globalHeight=height)

        self.__button = self.getNodeRender()

        
