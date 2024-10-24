# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # prefix sums encountered in current path
        from collections import defaultdict
        # The function of defaultdict(int) is to avoid errors when accessing nonexistent keys by automatically setting the value of a new key to 0
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # Can remove sums[currSum - targetSum] prefix sums to get target
                count = sums[total - targetSum]

                # Add value of this prefix sum
                sums[total] += 1
                # Explore children
                count += dfs(root.left, total) + dfs(root.right, total)
                # Remove value of this prefix sum (path's been explored)
                sums[total] -= 1

            return count

        return dfs(root, 0)

# Function to build the tree from the list input
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

# Example test case
tree_nodes = [10,5,-3,3,2,None,11,3,-2,None,1]
target_sum = 8

root = build_tree(tree_nodes)
solution = Solution()
result = solution.pathSum(root, target_sum)

print("Output:", result)  # Expected Output: 3
