from types import MethodType
class Student(object):
    def __init__(self):
        print('Instance Created')
    __slots__= ('name','age','set_age') #用tuple定义允许绑定的属性名称

Tracy = Student()
Tracy.age = 20

Bob = Student()
Bob.age = 30

print('Tracy\'s age is %d'%Tracy.age)
print('Bos\'s age is %d'%Bob.age)

def set_age(self,age):
    self.age = age

s = Student()
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

Ceaser = Student()
Student.set_age = set_age
Ceaser.set_age(33)
print('Ceaser\'s age is %d'%Ceaser.age)

'''
Ceaser.score = 99
print('Ceaser\'s score is %d'%Ceaser.score)
'''
class Xiaoming(Student):
    pass
xiaoming = Xiaoming
xiaoming.score = 100
print('xiaoming\' score is %d'%xiaoming.score)
