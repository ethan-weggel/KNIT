from abc import ABC, abstractmethod

class BaseNode(ABC):
    __identifier = 0
    def __init__(self, **kwargs):

        self.__inputSockets = []
        self.__inputIdentifiers = []
        self.__outputSockets = []
        self.__outputIdentifiers = []

        self.__data = []

        self.__intendedInputNumber = 0
        self.__intendedOutputNumber = 0

        self.__requiresData = False

        self.__outgoing = None
        self.__received = None

        self.__function = None
        self.__functionName = None

        self.__x = None
        self.__y = None

        if len(kwargs.keys()) == 0:
            pass
        else:
            for key in kwargs.keys():
                match key.lower():
                    case "data":
                        for element in kwargs["data"]:
                            self.__data.append(element)
                    case "numinputs":
                        self.__intendedInputNumber = kwargs["numinputs"]
                    case "numoutputs":
                        self.__intendedOutputNumber = kwargs["numoutputs"]
                    case "requiresdata":
                        self.__requiresData = kwargs["requiresdata"]
                    case "inputidentifiers":
                        for identifier in kwargs["inputidentifiers"]:
                            self.__inputIdentifiers.append(identifier)
                    case "outputidentifiers":
                        for identifier in kwargs["outputidentifiers"]:
                            self.__outputIdentifiers.append(identifier)
                    case "x":
                        self.__x = kwargs["x"]
                    case "y":
                        self.__y = kwargs["y"]
                    case _:
                        raise ValueError(f"Key word <{key}> not supported.")
        
        BaseNode.__identifier += 1
        self.__identifier = BaseNode.__identifier

        self.__type = "MID"
        for identifier in self.__inputIdentifiers:
            if identifier == -1:
                self.__type = "START"
        for identifier in self.__outputIdentifiers:
            if identifier == -2:
                self.__type = "END"

    def getType(self):
        return self.__type

    def getInputSockets(self, index=None):
        if index == None:
            return self.__inputSockets
        else:
            return self.__inputSockets[index]
        
    def getOutputSockets(self, index=None):
        if index == None:
            return self.__outputSockets
        else:
            return self.__outputSockets[index]
        
    def plugInput(self, node):
        self.__inputs.append(node)

    def plugOutput(self, node):
        self.__outputs.append(node)

    def unplugInput(self, index=None, node=None):
        if index == None and node != None:
            self.__inputs.remove(node)
        elif index != None and node == None:
            del self.__inputs[index]
        else:
            raise ValueError("Index or Node are either both set or incorrect values.")
        
    def unplugOutput(self, index=None, node=None):
        if index == None and node != None:
            self.__outputs.remove(node)
        elif index != None and node == None:
            del self.__outputs[index]
        else:
            raise ValueError("Index or Node are either both set or incorrect values.")
        
    def getIdentifier(self):
        return self.__identifier
    
    def getOutgoing(self):
        return self.__outgoing
    
    def getReceived(self):
        return self.__received
    
    def setOutgoing(self, value):
        self.__outgoing = value

    def setReceived(self, value):
        self.__received = value

    def getData(self):
        return self.__data
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value

    def getInputIdentifiers(self):
        return self.__inputIdentifiers
    
    def getOutputIdentifiers(self):
        return self.__outputIdentifiers
    
    def getSocketLoadingInputs(self):
        return self.__inputIdentifiersSocketLoading
    
    def getSocketLoadingOutputs(self):
        return self.__outputIdentifiersSocketLoading
    
    def deductNode(self, value, inputIdentifier=True):
        if inputIdentifier:
            self.__inputIdentifiersSocketLoading.remove(value)
        else:
            self.__inputIdentifiersSocketLoading.remove(value)
    
    def setFunction(self, function):
        self.__function = function

    def getFunction(self):
        return self.__function
    
    def setFunctionName(self, name):
        self.__functionName = name

    def getFunctionName(self):
        return self.__functionName

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def receive(self, nodePtr):
        pass

    @abstractmethod
    def send(self, nodePtr):
        pass

class Node(BaseNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def process(self, executingFunc):
        self.__outgoing = executingFunc(self)
    
    def receive(self):
        try:
            # received obj is iterable
            iter(self.__received)
            for element in self.__received:
                self.__data.append(element)
            self.__received = None
        except TypeError:
            # received obj is not iterable
            self.__data.append(self.__received)
            self.__received = None

    
    def send(self):
        if self.__outgoing != None:
            for nodePtr in self.getOutputs():
                nodePtr.setReceived(self.__outgoing)
            self.setOutgoing(None)
        else:
            print(f"Current node ({self.getIdentifier()}) is None.")


class EntryPoint:
    def __init__(self, hashVal, inputNode):
        self.__hash = hashVal

        self.__inputNode = inputNode

    def getHashId(self):
        return self.__hash
    
    def setHashId(self, value):
        self.__hash = value

    def getInputNode(self):
        return self.__inputNode
    
    def setInputNode(self, nodeObj):
        self.__inputNode = nodeObj

    def onStart(self, func):
        func()

class TerminationPoint:
    def __init__(self, hashVal, outputNode):
        self.__hash = hashVal

        self.__outputNode = outputNode

    def getHashId(self):
        return self.__hash
    
    def setHashId(self, value):
        self.__hash = value

    def getOutputNode(self):
        return self.__outputNode
    
    def setOutputNode(self, nodeObj):
        self.__outputNode = nodeObj

    def onStart(self, func):
        func()