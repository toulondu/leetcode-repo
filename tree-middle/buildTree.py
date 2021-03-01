# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 想到2种方法
# 第一种，前序的第一个元素为root，从第二个元素开始遍历前序，
# 将每个元素插入到正确的位置，新构建的树为res
# 判断方式是根据元素在中序中的idx和res中当前节点的idx对比并推进得到
# 结果：
# 执行用时：680 ms, 在所有 Python3 提交中击败了5.15%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了97.14%的用户


class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        res = TreeNode(preorder[0])
        preorder = preorder[1:]

        # 树中没有重复的元素，那就搞个map来存位置
        nMap = {}
        for i in range(len(inorder)):
            nMap[inorder[i]] = i

        def insertValue(num: int):
            current = res
            while True:
                isLeft = nMap[current.val] > nMap[num]
                if isLeft:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = TreeNode(num)
                        break
                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = TreeNode(num)
                        break

        for item in preorder:
            insertValue(item)
        return res

# 方法2思路很简单
# 以前序的第一个元素开始，在中序中找到它的位置，位于其左边的为左子树，右为右子树，左子树长l1，右子树长l2
# 那么在前序中，preorder[1:l1]为左子树，preorder[l1+1:]为右子树
# 以此对2边进行递归


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        res = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        preorder1 = preorder[1:idx+1]
        preorder2 = preorder[idx+1:]
        inorder1 = inorder[0:idx]
        inorder2 = inorder[idx+1:]

        res.left = self.buildTree(preorder1, inorder1)
        res.right = self.buildTree(preorder2, inorder2)
        return res

# 官方解法


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(
                preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(
                preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)


s = Solution1()
res = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(res.val, res.left.val, res.right.val,
      res.right.left.val, res.right.right.val)
