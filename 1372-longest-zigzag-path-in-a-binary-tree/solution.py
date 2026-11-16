# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        if not root or root.left is None and root.right is None:
            return 0

        self.maxlen = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.maxlen = max(self.maxlen, length)

            if direction =="left": # left -> right -> left
                dfs(node.right, "right", length + 1)
                dfs(node.left, "left", 1)
            else: # right -> left -> right
                dfs(node.left, "left", length + 1)
                dfs(node.right, 'right', 1)

        dfs(root.right, "right", 1)
        dfs(root.left, "left", 1)
        return self.maxlen
