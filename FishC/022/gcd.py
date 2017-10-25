class Solution(object):
    def __init__(self):
        pass
    def gcd(self,x,y):
        if y == 0:
            return x
        else:
            return self.gcd(y,x%y)

Test = Solution()
print(Test.gcd(36,24))
print(Test.gcd(10,7))
