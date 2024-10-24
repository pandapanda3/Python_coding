# leetcode 75: 1448. Count Good Nodes in Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root,val):
            if root:
                k = good(root.left, max(val, root.val)) + good(root.right, max(val, root.val))
                if root.val >= val:
                    k+=1
                return k
            return 0
        return good(root, root.val)