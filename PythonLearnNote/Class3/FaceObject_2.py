class Solution(object):
    def __init__(self,name,score):
        self.__name  = name
        self.__score = score

    def print_info(self):
        print("This Student Name is %s , and He's Score is %d"%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad Score')

if __name__ == "__main__":
    Student = Solution('Python',199)
    Student.print_info()
    print(Student.get_name())
    print(Student.get_score())
    Student.set_score(199)

