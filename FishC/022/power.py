class Solution(object):
    def __init__(self):
        pass
    def power(self,x,y):
        if y == 0:
            return 1
        elif y == 1:
            return x
        else:
            return x*(self.power(x,y-1))

if __name__ == '__main__':
    Test = Solution()
    print(Test.power(2,5))
    print(Test.power(10,3))
    print(Test.power(-2,3))
    print(Test.power(2,0))


