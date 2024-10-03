
import threading
import multiprocessing
import time
import warnings
import sys
from zimply import ZIMServer
import warnings
import requests
from bs4 import BeautifulSoup
import sys
warnings.filterwarnings("ignore", category=DeprecationWarning)

def retriever(node):
    class RAGToolKit:
        def __init__(self, port=9454):
            self.__port = port

        def extractTextFromHtml(self, htmlContent):
            soup = BeautifulSoup(htmlContent, 'html.parser')
            return soup.get_text()

        def isServerRunning(self):
            try:
                response = requests.get(f"http://localhost:{self.__port}/")
                return response.status_code == 200
            except requests.exceptions.RequestException:
                return False

        def fetchArticle(self, articleTitle, memoryLocationForReturnValue):
            if not self.isServerRunning():
                print("Server is not running. Unable to fetch content.")
                return

            req_url = f"http://localhost:{self.__port}/A/{articleTitle}"

            try:
                response = requests.get(req_url)
                response.raise_for_status() 

                contentsText = self.extractTextFromHtml(response.content)
                # print(f"--- Article Content: {articleTitle} ---\n{contentsText}")

                # assume this variable is a mutable container so it can be passed by reference rather than by value
                memoryLocationForReturnValue[0] = contentsText
                # print(memoryLocationForReturnValue)
                # return memoryLocationForReturnValue
            except requests.exceptions.RequestException as e:
                print(f"Failed to retrieve article '{articleTitle}': {e}")
                return
    class RAGZimServer:
        def __init__(self, port=9454, path="E:\\wikipedia_en_all_nopic_2024-06.zim"):
            print("__starting .ZIM server for R.A.G. engine__")
            self.__port = port
            self.__path = path
            self.__server = ZIMServer(self.__path, port=self.__port)

        def startServer(self):
            self.__server.start()

        def killServer(self):
            self.__server.stop_server()
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
               method(category, variable)

        def useTool(self, method_name, category):
            memory = [None]
            self.__toolKitThread = threading.Thread(target=self.startToolKitThread, args=(method_name, category, memory))
            self.__toolKitThread.start()
            self.__toolKitThread.join() 
            return memory

        def killManager(self):
            self.__server.killServer()
    
    manager = RAGManager()
    # staticPath = "E:\\wikipedia_en_all_nopic_2024-06.zim"
    # text = manager.useTool("fetchArticle", str(node.getData()[0]))

    returnData = [*node.getData()]

    for key in node.getData()[1].keys():
        value = node.getData()[1][key]
        try:
            returnData.append(manager.useTool("fetchArticle", str(value)))
        except Exception:
            continue


    manager.killManager()
    return returnData


