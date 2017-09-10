import unittest
import traceback
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def __init__(self):
        self.flag = 0
    def createLinkList(self):
        try:
            head = ListNode(-1)
            num = int(input('Please Input Non-Num To Create a LinkList:'))
            print('num = ',num)
            while(num>0):
                p = ListNode(num)
                p.next = head.next
                head.next = p
                num = int(input('Please Input Non-Num To Create a LinkList:'))
                print('num = ',num)
            print('Create Link List Done')
        except Exception:
            traceback.print_exc()
        finally:
            return head
    def printLinkList(self,head):
        print("prepare to print")
        p = head
        while(p is not None):
            print(p.val)
            p = p.next

    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(-1)
        p = head
        while l1 or l2:
            su = 0
            if l1:
                su += l1.val
                l1 = l1.next
            if l2:
                su += l2.val 
                l2 = l2.next
            su += self.flag
            print('su = ',su)
            self.flag =int(su/10)
            print('self.flag = ',self.flag)
            tmp = ListNode(-1)
            tmp.val = su%10
            print('tmp.val = ',tmp.val)
            p.next = tmp
            p = tmp
        if self.flag == 1:
            tmp = ListNode(self.flag)
            p.next = tmp
        return head
class TestSolution(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        Test = Solution()
        l1 = Test.createLinkList()
        Test.printLinkList(l1)
        print('---------------------')
        l2 = Test.createLinkList()
        Test.printLinkList(l2)
        print('---------------------')
        lv = Test.addTwoNumbers(l1.next,l2.next)
        print('lv = ',lv)
        Test.printLinkList(lv)
        pass

if __name__ == '__main__':
    unittest.main()
