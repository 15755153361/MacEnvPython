class Solution(object):
    def __init__(self):
        pass
    def Convert(self):
        while True:
            Input_Num = input("请输入一个整数(输入Q结束程序)：")
            if Input_Num == 'Q':
                return
            Ten_Num = int(Input_Num)
            if not isinstance(Ten_Num,int):
                return
            print('十进制->十六进制：%d->%s'% (Ten_Num,self.Convert16(Ten_Num)))
            print('十进制->八进制：  %d->%s'% (Ten_Num,self.Convert8(Ten_Num)))
            print('十进制->二进制:   %d->%s'% (Ten_Num,self.Convert2(Ten_Num)))
    
    def Convert16(self,Ten_num):   
        list_16 = []
        Res = ''
        while Ten_num:
            mod_16 = Ten_num % 16
            print('Ten_num = %d , mod_16 = %d'%(Ten_num,mod_16))
            if mod_16 <10:
               mod_16 = mod_16 
            elif mod_16==10:
                mod_16 = 'A'
            elif mod_16 == 11:
                mod_16 = 'B'
            elif mod_16 == 12:
                mod_16 = 'C'
            elif mod_16 == 13:
                mod_16 = 'D'
            elif mod_16 == 14:
                mod_16 = 'E'
            else:
                mod_16 = 'F'
            list_16.append(mod_16)
            Ten_num = Ten_num // 16
        list_16.reverse()
        print('list_16 = ',list_16)
        for i in list_16:
            Res += str(i)
        return '0x'+Res
    def Convert8(self,Ten_num):
        list_8 = []
        Res = ''
        while Ten_num:
            mod_8 = Ten_num % 8
            print('Ten_num = %d , mod_8 = %d'%(Ten_num,mod_8))
            list_8.insert(0,mod_8)
            Ten_num = Ten_num // 8
        print('list_8 = ', list_8)
        for i in list_8:
            Res += str(i)
        return '0o' + Res
    def Convert2(self,Ten_num):
        list_2 = []
        Res = ''
        while Ten_num:
            mod_2 = Ten_num % 2
            print('Ten_num = %d , mod_2 = %d'%(Ten_num,mod_2))
            list_2.insert(0,mod_2)
            Ten_num = Ten_num // 2
        print('list_2 = ', list_2)
        for i in list_2:
            Res += str(i)
        return 'ob' + Res
if __name__ == '__main__':
    Test = Solution()
    Test.Convert()
