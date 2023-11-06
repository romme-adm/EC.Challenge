import json
import unittest
from EC_Challenge_Sorting.Sorting import Sorting

from EC_Challenge_Utils import ProcessInputs
from EC_Challenge_Utils import DataInitializer


class TestOrdering(unittest.TestCase):    
    def test_outputs(self):
        datainitializer = DataInitializer.DataInitializer("./EC_Challenge_DataSources","inputsUT.json")
        base_set  = json.loads(  datainitializer.load_json_entries_base() )
        process_inputs = ProcessInputs.ProcessInputsForSorting("./entries_for_searchUT.txt")
        inputs = process_inputs.processInputs()
        ordering = Sorting(base_set)
        ordering.set_hashes()
        ordering.pre_search(inputs)
        ordering.do_search()
        ordering.order_by_priority()
        self.assertEqual(ordering.show_final_matrix()[0]["id"],12366)


if __name__ == '__main__':
    unittest.main()