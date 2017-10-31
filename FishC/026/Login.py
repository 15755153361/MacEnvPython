class Solution(object):
    def HelpInfo(self):
        print("|--- 新建用户：N／n ---|")
        print("|--- 登陆账号：E／e ---|")
        print("|--- 退出程序：Q／q ---|")
    def MainProcess(self):
        LogSys = {}
        while(True):
            self.HelpInfo()
            OpCode = input("|---请输入指令代码：")
            if OpCode == 'N' or OpCode == 'n':
                UserName = input("请输入用户名：")
                while (True):
                    if UserName in LogSys:
                        UserName = input("此用户名已经被使用，请重新输入：")
                    else:
                        break
                PassWord = input("请输入密码：")
                LogSys[UserName] = PassWord
                print("注册成功，赶紧试试登陆吧！")
            elif OpCode == 'E' or OpCode == 'e':
                UserName = input("请输入用户名：")
                if UserName in LogSys:
                    PassWord = input("请输入密码：")
                    if PassWord == LogSys[UserName]:
                        print("欢迎进入XXOO系统，请点击右上角X结束程序")
                    else:
                        print("密码错误")
            elif OpCode == 'Q' or OpCode == 'q':
                print("欢迎使用XXOO系统，期待您的再次光临")
                break
            else:
                print("未知指令，请按照要求输入")
if __name__ == '__main__':
    Test = Solution()
    Test.MainProcess()
