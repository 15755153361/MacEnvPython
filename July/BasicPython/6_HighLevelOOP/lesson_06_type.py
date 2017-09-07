
def __init__(self,name):
        self.name = name

def sayHello(self):
        print('Hello, %s!' % self.name)

Hello = type('Hello',(object,),dict(__init__=init,hello=sayHello)) 

h = Hello()
h.sayHello()

