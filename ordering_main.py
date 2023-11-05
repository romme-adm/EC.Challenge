from EC_Challenge_Utils import ProcessInputs
from EC_Challenge_Utils import DataInitializer
from EC_Challenge_Ordering import Ordering
import json

if __name__ == '__main__':
    datainitializer = DataInitializer.DataInitializer("./EC_Challenge_DataSources","inputs.json")
    base_set  = json.loads(  datainitializer.load_json_entries_base() )
    process_inputs = ProcessInputs.ProcessInputsForOrdering("./entries_for_search.txt")
    inputs = process_inputs.processInputs()
    ordering = Ordering.Ordering(base_set)
    ordering.set_hashes()
    ordering.pre_search(inputs)
    ordering.do_search()
    ordering.order_by_priority()
    ordering.show_final_matrix()