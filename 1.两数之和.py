#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        hash_map={}
        for index,item in enumerate(nums):
            num2=target-item
            if num2 in hash_map:  
            #判断hash表这里为字典是否有为num2的key
               return[index,hash_map[num2]]
            hash_map[item]=index
        return None


# @lc code=end

