"""
Clase principal para preprocesar texto,
dividir nodos de trabajo (en caso de m=True)
"""

import math
import time

class PreProcesor:
    elements_group=[]
    def __init__(self,text_content, partisions):
        self.text_to_analyze_array = text_content.split(' ')
        self.elements_count = len(self.text_to_analyze_array)
        self.partisions = partisions
        print ("Total de elementos : ", self.elements_count)

    def calculate_worker_nodes(self):
        print ("Calculando carga de trabajo...", )
        rows  =int( math.ceil(   self.elements_count / self.partisions ))
        print ("Particiones solicitadas : ", self.partisions, " Items por partision : ", rows)
        memory_fragments = []
        row_data = []
        x_pos=0
        for item in self.text_to_analyze_array:
            row_data.append( item )
            if x_pos == (rows-1):
                x_pos=0
                memory_fragments.append( row_data )
                row_data = []
            else:
                x_pos+=1
        memory_fragments.append( row_data )
        return memory_fragments

    ##Se cuentan numero de coincidencias por nodo (todas las palabras)
    def process_payload(self,memory_row):
        index=0
        key_value_text = {}
        while index < (len( memory_row )):
            word_item = memory_row[index]
            if key_value_text.get(word_item) is None:
                key_value_text[word_item] = 1
            else :
                key_value_text[word_item] = (key_value_text[word_item]+1)
            index+=1
        self.elements_group.append( key_value_text )
        return 0
    
    ##Se busca la palabra por particion despues de realizar el analisis de la información
    ##Se suma las apariciones por nodo
    def do_search(self,text_to_searching):
        count=0
        start_time = time.time()
        for data_row in self.elements_group:
            if data_row.get( text_to_searching ) is not None:
                count= count+data_row.get( text_to_searching )
        print ("Se encontraron [", count, "] coincidencias en ",(time.time() - start_time) ,"sg" )
