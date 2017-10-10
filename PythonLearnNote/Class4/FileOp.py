import os
class Solution(object):
    def __init__(self,path):
        self.path = path

    def WriteFile(self):
        f = open(path,'w')
        f.write('This is a Python File Op')
        f.close()
    
        with open(path,'a') as f:
            f.write('Hello , Python Pro')


    def ReadFile(self):
        f = open(path,'r')
        print(f.read())
        f.close()

        with open(path,'r') as f:
            print(f.read())

if __name__ == '__main__':
    path = input('Please Input A Exist Path:')

    FileOp = Solution(path)

    FileOp.WriteFile()

    FileOp.ReadFile()


