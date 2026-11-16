# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q = deque([root])
        max_sum = float('-inf')
        curr_lvl = 1
        ans_lvl = 1

        while q:
            qlen = len(q)
            lvl_sum = 0

            for i in range(qlen):
                node = q.popleft()
                lvl_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if lvl_sum > max_sum:
                max_sum = lvl_sum
                ans_lvl = curr_lvl
            curr_lvl +=1

        return ans_lvl

            


        