# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        val = l1.val + l2.val
        next = self.addTwoNumbers(l1.next, l2.next)
        if (val >= 10):
            val -= 10
            next = self.addTwoNumbers(next, ListNode(1))
        return ListNode(val, next)
