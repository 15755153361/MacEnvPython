import unittest
class Solution(object):
    def __init__(self,score):
        self.score = score
    
    def JudgeScoreLevel(self):
        score = self.score
        result = 'NA'
        if score>100 or score<0:
            print("Error: Please Check Input Score score = %d!"%score)
        elif score>90:
            result = 'A'
        elif score>80:
            result = 'B'
        elif score>70:
            result = 'C'
        elif score>60:
            result = 'D'
        else:
            result = 'E'
        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        Test = Solution(99)
        self.assertEqual('A',Test.JudgeScoreLevel())
    def test_02(self):
        Test = Solution(89)
        self.assertEqual('B',Test.JudgeScoreLevel())
    def test_03(self):
        Test = Solution(79)
        self.assertEqual('C',Test.JudgeScoreLevel())
    def test_04(self):
        Test = Solution(69)
        self.assertEqual('D',Test.JudgeScoreLevel())
    def test_05(self):
        Test = Solution(59)
        self.assertEqual('E',Test.JudgeScoreLevel())
    def test_06(self):
        Test = Solution(199)
        self.assertEqual('NA',Test.JudgeScoreLevel())

if __name__ == '__main__':
    unittest.main()
