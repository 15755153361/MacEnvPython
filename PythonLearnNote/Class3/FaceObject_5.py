from types import MethodType
class Student(object):
    def __init__(self):
        print('Instance Created')

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



