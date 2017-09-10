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
        p = head.next
        while(p is not None):
            print(p.val)
            p = p.next

    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p = ListNode(-1)
        tmp = l1.val + l2.val + self.flag
        if tmp >= 10:
            self.flag = 1
        else:
            self.flag = 0
        p.val = tmp%10
        print('p , p.val = ',p,p.val)
        p.next = self.addTwoNumbers(l1.next,l2.next)
        return p
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
        lv = Test.addTwoNumbers(l1,l2)
        print('lv = ',lv)
        Test.printLinkList(lv)
        pass

if __name__ == '__main__':
    unittest.main()
