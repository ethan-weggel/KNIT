from zimply import ZIMServer

class RAG_ZIM_SERVER:
    def __init__(self, port=9454, path="E:\\wikipedia_en_all_nopic_2024-06.zim"):
        print("__starting .ZIM server for R.A.G. engine__")
        self.__port = port
        self.__path = path
        self.__server = ZIMServer(self.__path, port=self.__port)

    def start_server(self):
        self.__server.start()
        print(f"__server started in background at http://localhost:{self.__port}__")

    def kill_server(self):
        self.__server.stop()

rag = RAG_ZIM_SERVER()

