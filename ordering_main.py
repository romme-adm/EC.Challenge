from EC_Challenge_Utils import ProcessInputs
from EC_Challenge_Utils import DataInitializer
import json

if __name__ == '__main__':
    datainitializer = DataInitializer.DataInitializer("./EC_Challenge_DataSources","inputs.json")
    base_set  = json.loads(  datainitializer.load_json_entries_base() )
    for i in base_set:
        print (i)
    inputs = ProcessInputs.ProcessInputsForOrdering("./entries_for_search.txt")
    for i in inputs.processInputs():
        print (i)
    