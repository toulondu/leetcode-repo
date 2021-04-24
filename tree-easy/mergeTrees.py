'''
617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
      if root1 is None: return root2

      def merged(node1:TreeNode, node2: TreeNode):
        if node2:
          node1.val = node1.val+node2.val

          if node1.left:
            merged(node1.left,node2.left)
          else:
            node1.left = node2.left
        
          if node1.right:
            merged(node1.right,node2.right)
          else:
            node1.right = node2.right

      merged(root1,root2)
      return root1

s = Solution()
n1 = TreeNode(1,TreeNode(3,TreeNode(5)),TreeNode(2))
n2 = TreeNode(2,TreeNode(1,None,TreeNode(4)),TreeNode(3,None,TreeNode(7)))
n3 = s.mergeTrees(n1,n2)

print(n3.right.left,n3.right.right.val)