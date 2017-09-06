class Prime1000(object):
    def __init__(self):
        self.Prime,self.Len = self.FindAllPrime(1000)
        self.count = -1
    
    def __iter__(self):
        print('call __iter__')
        return self

    def __next__(self):
        self.count+=1
        if self.count>=self.Len:
            raise StopIteration()
        return self.Prime[self.count]
            
    
    def FindAllPrime(self,n):
        result = list(range(n))
        output = []
        cnt    = 0
        upper  = round(pow(n,0.5))+1
        for i in range(2,upper):
            j = i * i
            while(j<n):
                result[j] = 0
                j += i
        result[1] = 0
        for i in range(n):
            if result[i]!=0:
                cnt+=1
                output.append(i)
        return output,cnt

if __name__ == '__main__':
    for i in Prime1000():
        print(i)
