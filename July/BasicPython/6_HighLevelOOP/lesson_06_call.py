class MyClass(object):
    def haha(self):
        print('HAHA!')
    def __call__(self):
        print('you call call cls() directly.')

if __name__ == '__main__':
    cls = MyClass()
    cls.haha()
    cls()
    print(callable(cls))
    print(callable(max))
    print(callable([1,2,3]))
    print(callable(str))
    print(callable(None))
