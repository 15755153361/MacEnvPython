class MyProperty(object):
    def __init__(self,fget = None, fset = None, fdel = None):
        print('__init__ fget = ',fget)
        print('__init__ fset = ',fset)
        print('__init__ fdel = ',fdel)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self,instance,cls):
        if self.fget:
            print('__get__')
            return self.fget(instance)

    def __set__(self,instance,value):
        print('__set__ self = ',self)
        print('__set__ instance = ',instance)
        print('__set__ value = ',value)
        if self.fset:
            print('__set__')
            return self.fset(instance,value)

    def __delete__(self,instance):
        if self.fdel:
            return self.fdel(instance)

    def getter(self,fn):
        print('getter fn = ',fn)
        self.fget = fn

    def setter(self,fn):
        print('setter fn = ',fn)
        self.fset = fn

    def deler(self,fn):
        self.fdel = fn

class Student(object):
    @MyProperty
    def score(self):
        return self._score
    print('-----------------------------')
    @score.setter
    def set_score(self,value):
        self._score = value

if __name__ == "__main__":
    SA = Student()
    SA.score = 99
    print(SA.score)
