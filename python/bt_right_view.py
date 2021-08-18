from collections import deque
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def computeLevel(self, queue):
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return level

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = self.computeLevel(queue)
            res.append(level[-1])

        return res

    def initTree(self):
        r = TreeNode()
        r.val = 1
        r.left = TreeNode()
        r.left.val = 2
        r.right = TreeNode()
        r.right.val = 3

        return r

s = Solution()
root = s.initTree()
res = s.rightSideView(root)

print(res)

