import pygame
import sys
import os
# from modules.components.node_render import NodeRender

nodeRenderPath = os.path.dirname("C:\\Users\\Ethan\\Documents\\Katherine\\Katherine-Node-Interfacing-Tool\\KNIT\\app\\modules\\components\\node_render.py")
sys.path.insert(0, nodeRenderPath)

import node_render

class Button(node_render.NodeRender):
    __Id = 0
    def __init__(self, node, x, y, width, height, color=(0,0,0), secondaryColor=(255,255,255), text="BUTTON", textColor=(0,0,0), func=None):
        super().__init__(node, x, y, globalWidth=width, globalHeight=height)

        self.__button = self.getNodeRender()

        self.__function = func

        self.__buttonColor = color
        self.__secondaryButtonColor = ()
        self.__textColor = textColor

        self.__text = text

        self.__id = Button.__Id
        Button.__Id += 1

    def getButtonId(self):
        return self.__id
    
    def click(self, func=None):
        if self.__function == None:
            self.__function = func

        self.__function()

    def getButton(self):
        return self.__button
    
    def getButtonColor(self):
        return self.__buttonColor
    
    def getTextColor(self):
        return self.__textColor
    
    def getText(self):
        return self.__text
    
    def setButtonColor(self, value):
        self.__buttonColor = value

    def setTextColor(self, value):
        self.__textColor = value

    def setText(self, value):
        self.__text = value

        
