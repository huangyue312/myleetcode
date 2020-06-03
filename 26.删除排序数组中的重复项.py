#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ##解法一 72ms 注意pop函数的复杂度为o(n)
        # if len(nums)==0:return 0
        # min=nums[0]
        # i=1
        # while i<len(nums):
        #     if nums[i]==min: 
        #         nums.pop(i)
        #     else: 
        #         min=nums[i]
        #         i=i+1

        # return len(nums)
        ##解法二
        if len(nums)==0:return 0
        s=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[s]=nums[i]
                s+=1
        return s





# @lc code=end

