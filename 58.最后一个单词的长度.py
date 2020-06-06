#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #解法一40ms
        # l=s.split(' ')
        # while  len(l)>0 and l[-1]=='':
        #     l.pop()
        # if len(l)==0 :return 0
        # return len(l.pop())
        ls = len(s)
        #解法一32ms
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow-=1
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast
# @lc code=end

