import random

class Solution(object):
    def __init__(self,num):
        self.num = num
        self.target = random.randint(10,100)
    def GuessNum(self):
        target = self.target
        guess_num = self.num
        g_count = 0
        while g_count<3:
            if guess_num == target:
                print("Congratulations, Well Done!")   
                break
            if guess_num > target:
                print("Your Input is Bigger!")
            if guess_num < target:
                print("Your Input is Smaller!")
            guess_num = int(input("Please Input Your Num: "))
            g_count+=1
        if g_count>=3:
            print("Sorry, you are wrong!")
if __name__ == '__main__':
    Num = int(input("Please Input Your Num: "))
    Test = Solution(Num)
    Test.GuessNum()


