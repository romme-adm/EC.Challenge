class DataInitializer:
    full_text=''
    def __init__(self,path, file_name):
        self.file_name = file_name
        self.path =path
    
    def load_text_to_processing(self):
        print ('Leyendo fuente de datos...')
        with open(  self.path + "/" + self.file_name ,'r',encoding="utf-8") as reader:
            self.full_text = reader.read().replace(".","").replace(",","").replace("\n"," ")
        return self.full_text
    