#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (37.95%)
# Likes:    246
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 84K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        # ##ord('A')=65 chr(65)='A'
        res=[]
        while n>0:
            res.append(chr(65+(n-1)%26))
            n=(n-1)//26
        res.reverse()
        return ''.join(res)

        # capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        # result = []
        # while n > 0:
        #     result.append(capitals[(n-1)%26])
        #     n = (n-1) // 26
        # result.reverse()
        # return ''.join(result)
# @lc code=end

