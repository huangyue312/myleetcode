#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (37.27%)
# Likes:    1012
# Dislikes: 0
# Total Accepted:    253K
# Total Submissions: 678.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # 解法一 利用zip 标记未ac
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans

        # #解法二 利用python中字符串大小比较
        # if not strs: return ""
        # s1 = min(strs)
        # s2 = max(strs)
        # for i,x in enumerate(s1):
        #     if x != s2[i]:
        #         return s2[:i]
        # return s1
                
        
# @lc code=end

