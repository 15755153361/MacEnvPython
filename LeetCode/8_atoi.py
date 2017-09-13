import unittest
class Solution(object):
    def myAtoi(self,str):
        str = str.strip()
        if len(str) == 0:
            return 0
        flag = 0
        num  = 0
        res_str = ''
        if str[0] == '+':
            flag = 1
        if str[0] == '-':
            flag = -1
        if flag == 0:
            if str[0]<'0' or str[0]>'9':
                return 0
        for i in range(0,len(str)):
            if i == 0 and flag != 0:
                pass
            else:
                if str[i]<'0' or str[i]>'9':
                    break
                else:
                    res_str+=str[i]
        if res_str != '':
            num = int(res_str)
        if flag == -1:
            if num>2147483648:
                num = 2147483648
            num = 0 - num
        else:
            if num > 2147483647:
                num = 2147483647
        return num

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase_01(self):
        Test = Solution()
        str_case = '+1234'
        tar_case = 1234
        self.assertEqual(Test.myAtoi(str_case),tar_case)

    def testCase_02(self):
        Test = Solution()
        str_case = '-1234'
        tar_case = -1234
        self.assertEqual(Test.myAtoi(str_case),tar_case)
    
    def testCase_03(self):
        Test = Solution()
        str_case = '123499999999999'
        tar_case = 2147483647
        self.assertEqual(Test.myAtoi(str_case),tar_case)
if __name__ == '__main__':
    unittest.main()
