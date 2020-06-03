#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #解法一 44 ms
        l=[]
        while head!=None:
            l.append(head.val)
            head=head.next
        l.pop(-n)
        p=h=ListNode(0)
        for i in l:
            h.next=ListNode(i)
            h=h.next
        return p.next
    
# @lc code=end

