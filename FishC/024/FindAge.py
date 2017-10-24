class Solution(object):
    def __init__(self,n):
        self.n = n

    def GetFiveAge(self):
        if self.n == 1:
            return 10
        else:
            self.n -= 1
            return self.GetFiveAge()+2

if __name__ == '__main__':
    Test = Solution(5)
    print(Test.GetFiveAge())

