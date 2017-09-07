import unittest

class MyDict(dict):
    pass

class TestMyDict(unittest.TestCase):
    def setUp(self):
        print('Test Begin')

    def tearDown(self):
        print('Test End')

    def test_init(self):
        md = MyDict(one=1,two=2)
        self.assertEqual(md['one'],1)
        self.assertEqual(md['two'],2)
    
    def test_nonthing(self):
        pass

if __name__ == '__main__':
    unittest.main()
