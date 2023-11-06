import unittest

from EC_Challenge_Utils.ProcessInputs import ProcessInputsForSearchCoincidences


class TestJsonValues(unittest.TestCase):
    inputs = ProcessInputsForSearchCoincidences()
    
    def test_json_reader(self):
        self.inputs.loadJsonInput("./ec_config.json")
        self.assertEqual(self.inputs.getWord(), 'digitales')
        self.assertEqual(self.inputs.getWorkersCount(), 4)
        self.assertEqual(self.inputs.getDataSourceFile(), 'source_text_for_coincidences.txt')
        self.assertEqual(self.inputs.getDataSourcePath(), './EC_Challenge_DataSources')
        self.assertEqual(self.inputs.getAllowMultiprocesingFlag(), False)
    

if __name__ == '__main__':
    unittest.main()