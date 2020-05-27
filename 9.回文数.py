#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.54%)
# Likes:    1036
# Dislikes: 0
# Total Accepted:    327.7K
# Total Submissions: 569.5K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #解法一 76ms 85.74% 13.7
        if x<0:
            return False
        else:
            re=int(str(x)[::-1])
            #result= True if re==x else False
            return True if re==x else False
        
        #解法二  92ms 50.48% 13.7
        # if x < 0:
        #     return False

        # ranger = 1
        # while x / ranger >= 10:
        #     ranger *= 10

        # while x:
        #     left = int(x / ranger)
        #     right = x % 10
        #     if left != right:
        #         return False
            
        #     x = int((x % ranger) /10)
        #     ranger /= 100

        # return True
# @lc code=end

