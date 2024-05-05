import json

class Reader:
    def __init__(self, filePath=""):
        self.__path = filePath
        self.__data = {}

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return self.__path
    
    def readModel(self):
        with open(self.__path, "r") as file:
            self.__data = json.load(file)
        # self.__data['nodes'] = 3

    def saveModel(self):
        with open(self.__path, "w") as file:
            json.dump(self.__data, file, indent=2)

    def getData(self):
        return self.__data
    
    def setData(self, newDataDict):
        self.__data = newDataDict
    

# reader = Reader("C:\\Users\\Ethan\\Documents\\KNIT\\workflows\\models\\model1\\model-one-workflow-one.json")
# reader.readModel()
# print(reader.getData()["1"]["x"])
