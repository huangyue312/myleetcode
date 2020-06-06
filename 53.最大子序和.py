#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:return 0
        s=s_max=nums[0]
        for item in nums[1:]:
            s=max(item,s+item)
            s_max=max(s_max,s)
        return s_max

# @lc code=end

