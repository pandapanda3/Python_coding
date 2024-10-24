from typing import Optional
# leetcode 75: 872. Leaf-Similar Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build the tree from a list of node values
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def collect_leaf_values(root, leaf_values):
            if not root:
                return
            if not root.left and not root.right:
                leaf_values.append(root.val)
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        collect_leaf_values(root1, leaf_values1)
        collect_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2

# Test with the example tree from the image using build_tree

# The tree in the image can be represented as follows:
# In level-order traversal (None represents missing nodes):
tree_nodes1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
tree_nodes2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

root1 = build_tree(tree_nodes1)
root2 = build_tree(tree_nodes2)

# Test the leafSimilar function
solution = Solution()
print(solution.leafSimilar(root1, root2))  # This should return True as the leaf sequences are the same
