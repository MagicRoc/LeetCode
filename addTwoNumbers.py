__author__ = 'MagicRoc'


class Solution:
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        ptr = result
        value = 0
        while True:
            if l1 != None:
                value += l1.val
                l1 = l1.next
            if l2 != None:
                value += l2.val
                l2 = l2.next
            ptr.val = value % 10
            value = value / 10
            if (l1 == None and l2 == None and value == 0):
                break
            else:
                new = ListNode(0)
                ptr.next = new
                ptr = ptr.next

        return result