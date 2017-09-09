import unittest
class Solution(object):
    def maxProfit(self, prices):
        cnt = len(prices)
        tmp_profit = 0
        max_profit = 0
        for i in range(cnt-1):
            if prices[i+1]-prices[i]>0:
                tmp_profit+=prices[i+1] - prices[i]
            #tmp_profit = max(tmp_profit+prices[i+1]-prices[i],0)
            #max_profit = max(tmp_profit,0)
        return tmp_profit

class TestSolution(unittest.TestCase):
    def setUp(self):
        Test = Solution()
        pass

    def tearDown(self):
        pass

    def Test_01(self):
        prices[1,3,6,9,2,1,4,5]
        max_profit = Test.max_profit(prices)
        self.assertEqual(prices,12)

    def Test_02(self):
        prices[1,5,6,4,21,1,4,5]
        max_profit = Test.max_profit(prices)
        self.assertEqual(prices,26)
if __name__ == '__main__':
    unittest.main()
