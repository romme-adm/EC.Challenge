"""
Clase leer los datos de los archivos fuentes
"""
class DataInitializer:
    full_text=''
    def __init__(self,path, file_name):
        self.file_name = file_name
        self.path =path
    ##Lee parrafo de archivo de texto para ejercicio 1
    def load_text_to_processing(self):
        print ('Leyendo fuente de datos...')
        with open(  self.path + "/" + self.file_name ,'r',encoding="utf-8") as reader:
            self.full_text = reader.read().replace(".","").replace(",","").replace("\n"," ")
        return self.full_text
    
    ##Lee entradas para posteriormente convertir a JSON para ejecicio 2
    def load_json_entries_base(self):
        with open(  self.path + "/" + self.file_name ,'r') as reader:
            self.full_text = reader.read()
        return self.full_text
    