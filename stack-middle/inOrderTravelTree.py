# -*- encoding: utf-8 -*-
'''
@FILE           :inOrderTravelTree.py
@TIME           :2020/05/03 15:23:01
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
'''

"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        nodes_res = []
        nodes_temp = [] # 存储左子树尚未遍历完全的节点
        while True:
            while root:
                nodes_temp.append(root)
                root = root.left

            # nodes_temp为空表示全部节点已经遍历完成，返回结果
            # 这个code block放在两个while中间是必须的，不太好解释，你们想象一下
            if not nodes_temp:
                return nodes_res

            while nodes_temp:
                # 此时nodes_temp中最后一个节点左子树已全部完成遍历，可以将它的val加入结果列表并将其从nodes_temp中删掉
                s = nodes_temp.pop()
                nodes_res.append(s.val)
                if s.right:
                    root = s.right
                    break

            



a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(1)
d = TreeNode(4)
e = TreeNode(6)
c.right = b
b.left = a
c.left = d
b.right = e

s = Solution()

print(s.inorderTraversal(c))