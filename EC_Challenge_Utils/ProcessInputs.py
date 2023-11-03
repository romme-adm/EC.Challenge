import json

class ProcessInputs:

    data = {}
    def loadJsonInput(self,path):
        with open(path, encoding='utf-8') as fh:
            self.data = json.load(fh)
            print (self.data)
    
    def getWord(self):
        return self.data["w"]

    def getWorkersCount(self):
        return self.data["n"]
    
    def getDataSourceFile(self):
        return self.data["df"]
    
    def getDataSourcePath(self):
        return self.data["dp"]
    
    def getAllowMultiprocesingFlag(self):
        return self.data["m"]
