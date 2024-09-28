# Leet Code 75： 700. Search in a Binary Search Tree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root: True not only for root == None, but also for other "falsy" values
        # such as root == 0 or root == [], root == "",root == (),root == {}
        if not root:
            return None
        if root.val == val:
            print(f'the value:{val}')
            return root
        elif root.val > val:
            print(f'the left val: {root.val}')
            return self.searchBST(root.left, val)
        elif root.val < val:
            print(f'the right val: {root.val}')
            return self.searchBST(root.right, val)
        
if __name__ == '__main__':
    # Construct the example binary search tree [4,2,7,1,3]
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    solution = Solution()
    result = solution.searchBST(root,2)