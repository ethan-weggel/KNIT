from RAG_Server import RAGZimServer
from RAG_ToolKit import RAGToolKit
import threading
import multiprocessing
import time
import warnings
import sys
warnings.filterwarnings("ignore", category=DeprecationWarning)

class RAGManager:
    def __init__(self):

        self.__server = None
        self.__toolKit = RAGToolKit()

        self.__serverThread = None
        self.__toolKitThread = None

        self.startServerThread()

    def instantiateServer(self):
        self.__server = RAGZimServer()

    def instantiateTookKit(self):
        self.__tookKit = RAGToolKit()

    def startServerThread(self, port=9454):
        self.__serverThread = threading.Thread(target=self.instantiateServer)
        self.__serverThread.start()

    def startToolKitThread(self, method, category, variable):
        method = getattr(self.__toolKit, method, None)
        if method:
            return method(category,variable)

    def useTool(self, method_name, category):
        memory = None
        self.__toolKitThread = threading.Thread(target=self.startToolKitThread, args=(method_name, category, memory))
        self.__toolKitThread.start()
        self.__toolKitThread.join() 
        return memory

    def killManager(self):
        self.__server.killServer()



        