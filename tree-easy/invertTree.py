'''
226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: return None

        def reverseNode(node:TreeNode):
          temp = node.left
          node.left = node.right
          node.right = temp
          
          if node.left: reverseNode(node.left)
          if node.right: reverseNode(node.right)

        reverseNode(root)
        return root

s = Solution()
n1 = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
n2 = TreeNode(2,TreeNode(1,None,TreeNode(4)),TreeNode(3,None,TreeNode(7)))
n3 = s.invertTree(n2)
print(n3.left.val,n3.right.val,n3.left.left.val,n3.left.right)