# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def f(node): # returns (size, sum)
            nonlocal ans

            if not node:
                return 0, 0

            left_sz, left_sum = f(node.left)
            right_sz, right_sum = f(node.right)

            if (left_sum + right_sum + node.val) // (left_sz + right_sz + 1) == node.val:
                ans += 1

            return left_sz + right_sz + 1, left_sum + right_sum + node.val

        f(root)
        return ans