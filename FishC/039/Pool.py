class Turtle(object):
    def __init__(self,x):
        self.num = x

class Fish(object):
    def __init__(self,y):
        self.num = y

class Pool(object):
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish   = Fish(y)

    def print_num(self):
        print("Pool has turtle %d , fish %d" % (self.turtle.num,self.fish.num))

if __name__ == '__main__':
    pool = Pool(1,10)
    pool.print_num()


