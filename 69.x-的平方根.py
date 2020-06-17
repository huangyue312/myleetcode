#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.73%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    162.1K
# Total Submissions: 418.3K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        right,left=x,0
        
        while left<=right:
            mid=(right+left)//2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            elif mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return mid
# @lc code=end

