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
        position=0;
        for i in self.data_matrix:
            hash =  str(i["id"]) +"_"+str(i["weight"])+"_"+str(i["width"])+"_"+str(i["height"])+"_"+str(i["length"])+"_"+str(i["cost"])+"_"+str(i["priority"])
            self.data[hash] = position
            position+=1
    
    def pre_search(self,entry):
        self.search_entries = []
        for i in entry:
           for idx in self.indexes:
               if i.get(idx) is not None:
                   self.search_entries.append([i.get(idx),i["op"],i["param"]])

    def do_search(self):
        position_prop=0
        position_op=1
        position_value = 2

        for i in (self.search_entries):
            index_pos = self.indexes[ i[position_prop] ]
            print (i[position_prop])
            for mtx in self.data:
                achieve = self.decide_operacion(mtx.split("_")[index_pos],i[position_op],i[position_value] )
                #print (mtx.split("_")[index_pos],i[position_op],i[position_value],achieve)
                if achieve:
                    print (self.data[mtx])

    
    def decide_operacion(self,value_of_mtx,op,param):
        if op == "=":
            return value_of_mtx == param
        if op == "<=":
            return  value_of_mtx <= param
        if op == ">=":
            return  value_of_mtx >= param