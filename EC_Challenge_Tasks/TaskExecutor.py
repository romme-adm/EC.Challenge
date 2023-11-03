import concurrent.futures
class TaskExecutor:

    def __init__(self,pre_procesor_instance, params):
        self.pre_procesor_instance = pre_procesor_instance
        self.params = params

    def execute_multiprocesing(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as e:
            processors = [e.submit(self.pre_procesor_instance.process_payload, _p) for _p in self.params]
            results = [future.result() for future in concurrent.futures.as_completed(processors)]
            print(results)
            
    def execute_search(self,word_to_search):
         self.pre_procesor_instance.do_search(word_to_search)
