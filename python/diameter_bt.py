class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution :
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root):

        if root is None:
            return 0

        hl = self.height(root.left)
        hr = self.height(root.right)
        hR = hl + hr

        dl = self.diameterOfBinaryTree(root.left)
        dr = self.diameterOfBinaryTree(root.right)

        return max(hR, max(dl, dr))



# class Solution(object):
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#
#         self.output = 0
#
#         def depth(node, dist):
#
#             if not node.left and not node.right:
#                 return dist
#
#             if node.left and node.right:
#                 l = depth(node.left, 1)
#                 r = depth(node.right, 1)
#                 self.output = max(self.output, l + r)
#                 return max(dist + l, dist + r)
#
#             if node.left:
#                 return depth(node.left, dist + 1)
#
#             if node.right:
#                 return depth(node.right, dist + 1)
#
#         across_root = depth(root, 0)
#         self.output = max(self.output, across_root)
#
#         return self.output

s = Solution()

root = TreeNode()
right = TreeNode()
left = TreeNode()
root.right = right
root.left = left

res=s.diameterOfBinaryTree(root)

print(str(res))