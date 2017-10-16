import random as r

class Fish(object):
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("My Location is (%d,%d)"%(self.x,self.y))

class GoldFish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("My Dream is Eat Everyday...")
            self.hungry = False
        else:
            print("I am Full...")


if __name__ == "__main__":
    fish = Fish()
    fish.move()
    shark = Fish()
    shark.eat()
    shark.move()
