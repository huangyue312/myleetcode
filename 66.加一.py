#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        l=[]
        num=1
        p=0
        while len(digits)>0:
            num=num+digits.pop()*10**p
            p+=1
        # for j in str(num):
        #     l.append(int(j))
        return [int(j) for j in str(num)]
        



# @lc code=end

