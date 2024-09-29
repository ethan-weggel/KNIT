from zimply import ZIMServer
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

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

# server = RAGZimServer()
