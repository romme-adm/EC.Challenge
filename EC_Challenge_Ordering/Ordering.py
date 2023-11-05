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
        self.coincidences_array=[]
        for i in (self.search_entries):
            index_pos = self.indexes[ i[position_prop] ]
            #print (i[position_prop])
            for mtx in self.data:
                achieve = self.decide_operacion(mtx.split("_")[index_pos],i[position_op],i[position_value] )
                #print (mtx.split("_")[index_pos],i[position_op],i[position_value],achieve)
                if achieve:
                    self.coincidences_array.append(self.data_matrix[self.data[mtx]])


    
    def show_new_matrix():
        print ("algo")

    
    def decide_operacion(self,value_of_mtx,op,param):
        if op == "=":
            return value_of_mtx == param
        if op == "<=":
            return  value_of_mtx <= param
        if op == ">=":
            return  value_of_mtx >= param
    
    def order_by_priority(self):
        size_of_coincidences_array= len(self.coincidences_array)
        swapped = False
        for ca in range(size_of_coincidences_array):
            intenal_range = (size_of_coincidences_array - ca - 1)
            for internal_ca in range(0,intenal_range):     
                if self.coincidences_array[internal_ca]["priority"] < self.coincidences_array[internal_ca + 1]["priority"]:
                    self.coincidences_array[internal_ca+1],self.coincidences_array[internal_ca] = self.coincidences_array[internal_ca],self.coincidences_array[internal_ca+1]
                    swapped = True
            if not swapped:
                return
        return self.coincidences_array