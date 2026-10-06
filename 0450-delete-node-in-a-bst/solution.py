# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        #1. Base Cases- For BST if key less than root go left else right
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        #2. if there is no left node return right and vice-versa
        if not root.left :
            return root.right
        if not root.right :
            return root.left

        nxt = root.right
        while nxt.left:
            nxt = nxt.left
        nxt.left = root.left

        root = root.right
        return root
        

        