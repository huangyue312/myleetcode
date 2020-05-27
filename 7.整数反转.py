#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.20%)
# Likes:    1898
# Dislikes: 0
# Total Accepted:    359.3K
# Total Submissions: 1.1M
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x<0  else 1
        s=str(x*flag)
        num=int(s[::-1])  #该法64ms
        # num=0
        # while len(s)>0:
        #     num=num+int(s.pop())*(10**(len(s))) #该法52ms
        num=num*(num<2**31)*(num>-(2**31))*flag
        return num

# @lc code=end