class Solution(object):
    def Dec2Bin(self,Dec):
        result = ' '
        if Dec:
            return self.Dec2Bin(Dec//2) + str(Dec%2)
        else:
            return result
    
    def Dec2Oct(self,Dec):
        result = ' '
        if Dec:
            return self.Dec2Oct(Dec//8) + str(Dec%8)
        else:
            return result

    def Dec2Six(self,Dec):
        result = ' '
        if Dec:
            return self.Dec2Six(Dec//16) + str(self.JudgeSix(Dec%16))
        else:
            return result
    def JudgeSix(self,Num):
        if Num == 10:
            return 'A'
        elif Num == 11:
            return 'B'
        elif Num == 12:
            return 'C'
        elif Num == 13:
            return 'D'
        elif Num == 14:
            return 'E'
        elif Num == 15:
            return 'F'
        else:
            return Num
    

if __name__ == '__main__':
    Test = Solution()
    print('61 convert to bin is %s'%Test.Dec2Bin(62))
    print('5  convert to bin is %s'%Test.Dec2Bin(5))

    print('61 convert to Oct is %s'%Test.Dec2Oct(62))
    print('5  convert to Oct is %s'%Test.Dec2Oct(5))


    print('61 convert to Six is %s'%Test.Dec2Six(62))
    print('5  convert to Six is %s'%Test.Dec2Six(5))
