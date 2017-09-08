import unittest

class Solution(object):
    def maxProfit(self, prices):
        cnt = len(prices)
        max_profit = 0
        for i in range(cnt):
            for j in range(i,cnt):
                if max_profit < prices[j] - prices[i]:
                    max_profit = prices[j] - prices[i]
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

