from EC_Challenge_ProcessCoincidences import PreProcesor
from EC_Challenge_Tasks import TaskExecutor
from EC_Challenge_Utils import ProcessInputs
from EC_Challenge_Utils import DataInitializer
import time

        

class Principal:
    process_input_instance={}
    def __init__(self, process_input_instance):
        self.process_input_instance = process_input_instance

    def run(self):
        initializer = DataInitializer.DataInitializer(self.process_input_instance.getDataSourcePath(),self.process_input_instance.getDataSourceFile())

        text_content =  initializer.load_text_to_processing()
        preprocesor_instance = PreProcesor.PreProcesor(text_content,self.process_input_instance.getWorkersCount())
        worker_nodes = preprocesor_instance.calculate_worker_nodes()
        word_to_search = self.process_input_instance.getWord()
        
        
        if self.process_input_instance.getAllowMultiprocesingFlag():
            print ("Dividiendo carga de trabajo en :" ,self.process_input_instance.getWorkersCount(),"workers")
            task_executor = TaskExecutor.TaskExecutor(preprocesor_instance,worker_nodes)
            start_time = time.time()
            task_executor.execute_multiprocesing()
            print("->","--- %s seconds ---" % (time.time() - start_time))
            task_executor.execute_search(word_to_search)

            return

        print ("Carga de trabajo en un solo worker")
        start_time = time.time()
        for wp in worker_nodes:
            preprocesor_instance.process_payload(wp)
        print("->","--- %s seconds ---" % (time.time() - start_time))
        preprocesor_instance.do_search(word_to_search)


if __name__ == '__main__':
    inputs = ProcessInputs.ProcessInputsForSearchCoincidences()
    inputs.loadJsonInput("./ec_config.json")
    Principal(inputs).run()


