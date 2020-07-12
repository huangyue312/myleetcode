#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res=[]
        self.bfs(0,root,res)
        return res
    def bfs (self,c,treenode,res):
        if treenode:
            #c=c+1 
            if len(res)<c+1:
                res.insert(0,[])
            res[-(c+1)].append(treenode.val)
            self.bfs(c+1,treenode.left,res)
            self.bfs(c+1,treenode.right,res)
            

        
        
                

# @lc code=end

