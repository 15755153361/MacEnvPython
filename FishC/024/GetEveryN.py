import unittest
class Solution(object):
    def __init__(self):
        pass
    
    def ConvertNum(self,num):
        result = ''
        if num:
            return self.ConvertNum(num//10) + str(num%10)
        else:
            return result

    def ResList(self,num):
        Num_str = self.ConvertNum(num)
        Str_list = list(Num_str)
        print('Str_list = ',Str_list)
        Num_list = []
        for i in Str_list:
            Num_list.append(int(i))          
        return Num_list        

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01_ConvertNum(self):
        Test = Solution()
        Result = (Test.ResList(12345))
        print('Result = ',Result)
        self.assertEqual([1,2,3,4,5],Result)

    def test_02_ConvertNum(self):
        Test = Solution()
        Result = (Test.ResList(123456789))
        print('Result = ',Result)
        self.assertEqual([1,2,3,4,5,6,7,8,9],Result)
if __name__ == '__main__':
    unittest.main()




