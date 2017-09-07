import unittest

class MyDict(dict):
    pass

class TestMyDict(unittest.TestCase):
    def test_init(self):
        md = MyDict(one=1,two=2)
        self.assertEqual(md['one'],1)
        self.assertEqual(md['two'],2)

if __name__ == '__main__':
    unittest.main()
