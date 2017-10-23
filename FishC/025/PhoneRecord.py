class Solution(object):
    def __init__(self):
        print('''
        |---欢迎进入通讯录程序---|
        |--- 1:查询联系人资料 ---|
        |--- 2:插入新的联系人 ---|
        |--- 3:删除已有联系人 ---|
        |--- 4:查询全部联系人 ---|
        |--- 5:退出通信录程序 ---|
        
        ''')
    def MainProcess(self):
        while True:
            Oper = input('请输入相关的指令代码：')
            if(Oper == '1'):
               self.SearchP()
            elif(Oper == '2'):
                self.InsertP()
            elif(Oper == '3'):
                self.DeleteP()
            elif(Oper == '4'):
                self.ShowAllContact()
            elif(Oper == '5'):
                print('|---感谢使用通信录程序---|')
                break
            else:
                print('|---情输入1、2、3、4进行相关操作---|')
        return
    def ShowAllContact(self):
        if not MyContact:
            print("当前通讯录位空")
        else:
            print(MyContact)
    def SearchP(self):
        Name = input("请输入联系人姓名：")
        if Name in MyContact:
            print("%s : %s"%(Name,MyContact[Name]))
        else:
            print('您要查找的联系人不存在')

    def InsertP(self):
        Name = input("请输入联系人姓名：")
        if Name in MyContact:
            print("您输入的姓名在通讯录中已经存在 -->> %s : %s"%(Name,MyContact[Name]))
            while True:
                Modify = input("是否修改用户资料(YES/NO)：")
                if(Modify == 'YES'):
                    Phone = input("请输入用户的联系电话：")
                    MyContact[Name] = Phone
                    break
                elif(Modify == 'NO'):
                    break
                else:
                    pass
        else:
            Phone = input("请输入用户联系电话：")
            MyContact[Name] = Phone

    def DeleteP(self):
        Name = input("请输入联系人姓名：")
        if Name in MyContact:
            MyContact.pop(Name)
        else:
            print('您要删除的联系人不存在')

if __name__ == '__main__':
    MyContact = {}
    Test = Solution()
    Test.MainProcess()


