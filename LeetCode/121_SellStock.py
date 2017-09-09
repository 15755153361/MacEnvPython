import unittest

class Solution(object):
    def maxProfit(self, prices):
        cnt = len(prices)
        max_profit = 0
        tmp_profit = 0
        for i in range(cnt-1):
            tmp_profit = max(tmp_profit+prices[i+1]-prices[i],0)
            max_profit = max(max_profit,tmp_profit)
        return max_profit

class TestSolution(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_maxProfit(self):
        Test = Solution()
        prices = [7,1,5,3,6,4]
        self.assertEqual(Test.maxProfit(prices),5)

    def test_02_maxProfit(self):
        Test = Solution()
        prices = [1,2,3,4,5,6,7]
        self.assertEqual(Test.maxProfit(prices),6)

    
    def test_03_maxProfit(self):
        Test = Solution()
        prices = [7,6,5,4,3,2,1]
        self.assertEqual(Test.maxProfit(prices),0)
if __name__ == '__main__':
    unittest.main()

