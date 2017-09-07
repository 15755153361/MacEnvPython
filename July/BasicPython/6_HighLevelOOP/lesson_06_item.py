class Fib100:
    def __init__(self):
        print('call __init__')
        self._1 , self._2 = 0,1

    def __iter__(self):
        print('call __iter__')
        return self

    def __next__(self):
        print('call __next__')
        self._1 , self._2 = self._2, self._1 + self._2
        if self._1 > 10:
            raise StopIteration()
        return self._1

if __name__ == '__main__':
    for i in Fib100():
        print(i)
