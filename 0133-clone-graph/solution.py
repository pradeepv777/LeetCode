"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # maps the original key to dupe key = {original: dupe}
        maps = {}
        # Traverse from current node (curr) to rest
        def dfs(curr):
            if curr in maps:
                return maps[curr]
            copy = Node(curr.val)
            maps[curr] = copy

            # Clone the neighbbors 
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
        