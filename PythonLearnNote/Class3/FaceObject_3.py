class Animal(object):
    def Base(self):
        print('Please Call Me Animal...')

    def Run(self):
        print('Aniaml is Running...')

class Dog(Animal):
    def Run(self):
        print('Dog is Running...')

class Cat(Animal):
    def Run(self):
        print('Cat is Running...')


animal = Animal()
animal.Base()
animal.Run()

dog = Dog()
dog.Base()
dog.Run()

cat = Cat()
cat.Base()
cat.Run()

