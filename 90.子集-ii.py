#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets=[[]]
        nums.sort()
        for i in range(1,len(nums)+1): #子集里有i个元素
            j=0
            l=[]
            while j<len(nums)
                l.appned(nums[j+i])
                j+=1
            if nums[i]!=nums[i-1]:
               

                


# @lc code=end

