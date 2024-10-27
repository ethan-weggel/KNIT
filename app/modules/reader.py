import json
import os

class Reader:
    def __init__(self, filePath=""):
        self.__path = filePath
        self.__data = {}

    def setPath(self, path):
        self.__path = path

    def getPath(self):
        return self.__path
    
    def readModel(self):
        for dirpath, _, filenames in os.walk(".."):
            if self.__path in filenames:
                self.__workflowPath = os.path.join(dirpath, self.__path)
                with open(self.__workflowPath, "r") as file:
                    print("Found workflow file")
                    self.__data = json.load(file)

    def saveModel(self):
        with open(self.__workflowPath, "w") as file:
            json.dump(self.__data, file, indent=2)

    def getData(self):
        return self.__data
    
    def setData(self, newDataDict):
        self.__data = newDataDict
    

# reader = Reader("C:\\Users\\Ethan\\Documents\\KNIT\\workflows\\models\\model1\\model-one-workflow-one.json")
# reader.readModel()
# print(reader.getData()["1"]["x"])
