class Solution(object):
    def __init__(self,name,score):
        self.name  = name
        self.score = score

    def print_info(self):
        print("This Student Name is %s , and He's Score is %d"%(self.name,self.score))

if __name__ == "__main__":
    Student = Solution('linwang',99)
    Student.print_info()



