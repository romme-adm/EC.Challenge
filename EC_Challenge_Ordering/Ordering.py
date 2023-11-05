import json


class Ordering:

    def __init__(self,data_matrix):
        self.data_matrix = data_matrix
        self.indexes = {
            "id":0,
            "weight":1,
            "width":2,
            "height":3,
            "length":4,
            "cost":5,
            "priority":6
            }
    
    def set_hashes(self):
        self.data={}
        for i in self.data_matrix:
            hash =  str(i["id"]) +"_"+str(i["weight"])+"_"+str(i["width"])+"_"+str(i["height"])+"_"+str(i["length"])+"_"+str(i["cost"])+"_"+str(i["priority"])
            self.data[hash] = i
    
    def do_search(self,entry):
       print (entry)