class Solution(object):
    def aDivisionb(self,a,b):
        try:
            print('try...')
            r = a/b
            print('result = %d'%r)
        except ValueError as e:
            print('ValueError: ',e)
        except ZeroDivisionError as e:
            print('ZeroDivisionError: ',e)
        else:
            print('no error!')
        finally:
            print('finally...')
        print('END...')

if __name__ == '__main__':
    Test = Solution()
    Test.aDivisionb(10,2)
    print('------------------')
    Test.aDivisionb(10,0)
