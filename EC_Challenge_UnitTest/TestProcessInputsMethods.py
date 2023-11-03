import unittest
from EC_Challenge_Utils import ProcessInputs


class TestStringMethods(unittest.TestCase):
    inputs = ProcessInputs.ProcessInputs()
    
    def test_json_reader(self):
        self.inputs.loadJsonInput("./ec_config.json")
        self.assertEqual(self.inputs.getWord(), 'logística')
        self.assertEqual(self.inputs.getWorkersCount(), 5)
        self.assertEqual(self.inputs.getDataSourceFile(), 'source_text_for_coincidences.txt')
        self.assertEqual(self.inputs.getDataSourcePath(), './EC_Challenge_DataSources')
        self.assertEqual(self.inputs.getAllowMultiprocesingFlag(), True)


if __name__ == '__main__':
    unittest.main()