#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:return l2
        if l2==None:return l1
        while l1 and l2:
            if l1.val<=l2.val:
                h=ListNode(l1.val)
                h.next=self.mergeTwoLists(l1.next,l2)
                return h
            else:
                h=ListNode(l2.val)
                h.next=self.mergeTwoLists(l1,l2.next)
                return h


        
        
# @lc code=end

