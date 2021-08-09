from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def initTree(self):
        r = TreeNode()
        r.val = 1
        r.left = TreeNode()
        r.left.val = 2
        r.right = TreeNode()
        r.right.val = 3

        return r

    def calLevel(self, queue, curr_size):
        level = []
        for _ in range(curr_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)

        return level

    def rightSideView(self, root: TreeNode) :
        if not root:
            return None
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            level = self.calLevel(queue, len(queue))
            res.append(level[-1])

        return res



s = Solution()
root = s.initTree()
res = s.rightSideView(root)

print(res)