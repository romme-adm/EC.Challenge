import json

"""
Clase para procesar JSON de entrada para busqueda de coincidencias.
"""
class ProcessInputsForSearchCoincidences:

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

"""
Clase para procesar datos de entrada para ejercicio de busqueda y ordenamiento
"""
class ProcessInputsForSorting:
    def __init__(self,path):
        with open(  path  ,'r') as reader:
            self.full_text = reader.read()
    
    def processInputs(self):
        char_open_found = False
        expression = ''
        searches = []
        ##Se procesa texto para proceder a convertirlo a JSON /
        for i in  self.full_text.replace("(","{").replace(")","}"):
            if not char_open_found and i == '{':
                expression +=i
                char_open_found=True
                continue
            if char_open_found:
                expression +=i
            if char_open_found and i == '}':
                searches.append(expression)
                expression =''
                char_open_found = False
        criteries = []
        for i in searches:
            criteries_array = i.replace("{",'').replace("}",'').split(',')
            ##Se crea arreglo de criterios para un mejor manejo
            criteries.append({
                criteries_array[0].replace("'",''):criteries_array[0].replace("'",''),
                "op":criteries_array[1].replace("'",'').strip(),
                "param":criteries_array[2].strip()})
        return criteries
    