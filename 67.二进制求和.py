#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.69%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    88.1K
# Total Submissions: 167.1K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ##解法一 56ms'
        # flag=0
        # re=""
        # a=list(a)
        # b=list(b)
        # while flag or len(a)>0 or len(b)>0:
        #     nums_1= int(a.pop()) if len(a)>0 else 0
        #     nums_2= int(b.pop()) if len(b)>0 else 0
        #     sum_item =flag + nums_1 + nums_2
        #     item=sum_item % 2
        #     re=re+str(item)
        #     flag=sum_item//2
        # return(re[::-1])

        #解法二 递归 56ms
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1]=='1' and b[-1]=='1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        elif a[-1]=='0' and b[-1]=='0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'
            
# @lc code=end

