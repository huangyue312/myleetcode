#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.02%)
# Likes:    1305
# Dislikes: 0
# Total Accepted:    103.7K
# Total Submissions: 203.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height) -> int:
        stack=[]
        a=0
        if len(height)<3: return 0
        for i in range(0,len(height)):
            while len(stack)>0 and height[i]>height[stack[-1]]:
                top=stack.pop()
                if len(stack)==0: break
                h=min(height[i],height[stack[-1]])-height[top]
                s=i-stack[-1]-1
                a=a+(h*s)
            stack.append(i)
        return a
    

# @lc code=end

