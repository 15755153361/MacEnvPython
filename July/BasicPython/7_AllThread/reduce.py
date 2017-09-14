from functools import reduce
import unittest
class Solution(object):
    def __init__(self,list_num):
        self.list_num = list_num
    def CalcAverage(self):
        positive_num_avg = 0
        positive_num_cnt = 0
        positive_num_sum = 0
        for i in self.list_num:
            if i > 0:
                positive_num_sum+=i
                positive_num_cnt+=1
        if positive_num_cnt > 0:
            positive_num_avg = positive_num_sum/positive_num_cnt
        return positive_num_avg

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase_01(self):
        list_num = [2,-5,9,7,-2,5,3,1,0,-3,8]
        Test = Solution(list_num)
        res_tar  = 5
        self.assertEqual(res_tar,Test.CalcAverage())
    def testCase_02(self):
        list_num = [2,-5,9,7,-2,5,3,1,0,-3,8]
        res_tar = 5
        tmp_sum = reduce(lambda x,y:x+y,filter(lambda x : x>0,list_num))
        tmp_cnt = len(list(filter(lambda x :x >0 , list_num)))
        print('tmp_sum = ',tmp_sum,'tmp_cnt = ',tmp_cnt)
        self.assertEqual(tmp_sum/tmp_cnt,res_tar)
if __name__ == '__main__':
    unittest.main()

