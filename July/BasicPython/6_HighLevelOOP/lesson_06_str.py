class MyClass(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        print('print wiil call __str__ first.')
        return 'Hello ' + self.name
    
print(MyClass('Tom'))	
print(__name__)
