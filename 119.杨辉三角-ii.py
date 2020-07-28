#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.25%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    61K
# Total Submissions: 99.3K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:return [1]
        if rowIndex==1:return [1,1]
        l=[1,1]
        for i in range(2,rowIndex+1):
            l=[l[j]+l[j-1] for j in range(1,i)]
            l.append(1)
            l.insert(0,1)
        return l



# @lc code=end

