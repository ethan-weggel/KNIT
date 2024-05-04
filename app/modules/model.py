from modules.node import Node
from pathlib import Path
import importlib
import inspect
import os
import re

class Model:
    __id = 1
    def __init__(self, reader):
        self.__id = Model.__id
        Model.__id += 1

        self.__reader = reader
        self.__data = self.__reader.getData()

        self.__nodeCount = self.__data["nodes"]

        self.__socketQueue = self.__data["socketQueue"]

        self.__nodes = []
        self.__functions = {}

        self.__entryPoint = None
        self.__terminationPoint = None
        
        # print(self.__data)
        for i in range(1, self.__data["nodes"]+1):
            node = Node(requiresdata=False,
                        x=self.__data[str(i)]["x"],
                        y=self.__data[str(i)]["y"],
                        numinputs=self.__data[str(i)]["numinputs"],
                        numoutputs=self.__data[str(i)]["numoutputs"],
                        inputidentifiers=self.__data[str(i)]["inputIdentifiers"],
                        outputidentifiers=self.__data[str(i)]["outputIdentifiers"])
            self.__nodes.append(node)

    def __str__(self):
        fmt = ""
        fmt += "null --> "
        for node in self.__nodes:
            fmt += str(node.getIdentifier()) + " --> "
        fmt += "null"
        return fmt

    def getId(self):
        return self.__id
    
    def getNodes(self):
        return self.__nodes
    
    def getfunctionName(self, text):
        pattern = r"def\s+(\w+)\s*\("
        match = re.search(pattern, text)
        if match:
            function_name = match.group(1)
            return function_name
    
    def getSocketQueue(self):
        return self.__socketQueue
    
    def setSocketQueue(self, queue):
        self.__socketQueue = queue

    def getFunctions(self):
        return self.__functions
    
    def loadZipFunctions(self):

        zipFunctionPath = Path(self.__reader.getData()["zipFunctions"])
        for filePath in zipFunctionPath.iterdir():
            with open(filePath, 'r') as file:
                functionText = file.read()
                functionName = self.getfunctionName(functionText)
                print(functionName)
                try:
                    exec(functionText, globals())
                    parsedFunction = globals()[functionName]
                except Exception as e:
                    print("Error parsing function:", e)
                self.__functions[functionName] = parsedFunction

        funcNodeZIP = zip(self.__nodes, list(self.__functions.keys()))
        for node, function in funcNodeZIP:
            node.setFunction(self.__functions[function])
            node.setFunctionName(function)

    def saveModel(self, nodeRenderings, socketRenderings):
        '''
        NOTE: this save feature modifies existing data dict and passes back to 
        reader which then saves using its own save feature. Only changes node 
        positions as of (4/21).
        '''

        renderNodeZIP = zip(nodeRenderings, self.__nodes)
        for render, node in renderNodeZIP:
            node.setX(render.getX())
            node.setY(render.getY())

        
        for index, node in enumerate(self.__nodes, start=1):
            self.__data[str(index)]["x"] = node.getX()
            self.__data[str(index)]["y"] = node.getY()
        
        socketQueueIDs = [socket.getRenderId() for socket in socketRenderings]
        self.__data["socketQueue"] = socketQueueIDs

        self.__reader.setData(self.__data)
        self.__reader.saveModel()

    


    