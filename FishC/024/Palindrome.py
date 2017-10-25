class Solution(object):
    def __init__(self):
        pass

    def Palindrome(self,name,start,end):
        if start>=end:
            return 1
        else:
            if name[start] == name[end]:
                return self.Palindrome(name,start+1,end-1)
            else:
                return 0

if __name__ == '__main__':
    name = input("Please Input a Str:")
    length = len(name)
    Test = Solution()
    print(Test.Palindrome(name,0,length-1))
