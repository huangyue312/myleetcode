#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.57%)
# Likes:    529
# Dislikes: 0
# Total Accepted:    162.4K
# Total Submissions: 355.9K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ##解法一，顺序搜索 36ms
        # for i in range(0,len(nums)):
        #     if nums[i]>=target:return i
        #     elif nums[i]==target:return i
        # return i+1

        ##解法二，二分查找 36ms
        l,r= 0,(len(nums)-1)
        #mid=int(r+l)/2
        while l<=r:
            mid=int((r+l)/2)
            if nums[mid]==target:return mid
            if nums[mid]>target:r=mid-1
            else :l=mid+1
        return l

        

# @lc code=end

