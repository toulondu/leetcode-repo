'''
652. 寻找重复的子树
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。
'''
# Definition for a binary tree node.
from typing import List
import collections
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    count = collections.Counter()
    res = []
  
    def handleTree(root: TreeNode):
      if not root: return '#'
      # 这里被坑了，开始是直接把三个值拼接在一起作为key，结果1和11这样的数字一拼，跟11和1拼的结果屎一样的。所以需要加一个，作为分隔符
      key = "{},{},{}".format(root.val,handleTree(root.left),handleTree(root.right))
      count[key]+=1

      if count[key]==2: res.append(root)

      return key
    
    handleTree(root)
    return res

tree = TreeNode(2,TreeNode(1,TreeNode(11)), TreeNode(11,TreeNode(1)))
s = Solution();
print(s.findDuplicateSubtrees(tree))