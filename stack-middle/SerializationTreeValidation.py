# -*- encoding: utf-8 -*-
'''
@FILE           :SerializationTreeValidation.py
@TIME           :2020/05/03 13:51:29
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
'''
"""
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:

输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
示例 2:

输入: "1,#"
输出: false
示例 3:

输入: "9,#,#,1"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class Solution:
#     tree = 1
#     def isValidSerialization(self, preorder: str) -> bool:
#         if not str:
#             return False
#         preorder = preorder.split(",")

#         if len(preorder)==1 and preorder[0]=='#':
#             return True

#         node_list = []
#         for c in preorder:
#             if not self.tree:
#                 return False

#             if c=='#':
#                 if not node_list:
#                     return False
#                 self.trace_back(node_list)
#             else:
#                 node_list.append(2)
#         return len(node_list)==0
    
#     def trace_back(self, node_list):
#         if node_list:
#             node_list[-1]-=1
#             if node_list[-1]==0:
#                 node_list.pop()
#                 self.trace_back(node_list)
#         else:
#             self.tree-=1

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not str:
            return False
        preorder = preorder.split(",")
        num = 1
        for c in preorder:
            if num==0: return False
            if c=='#':
                num-=1
                if num<0: return False
            else:
                num+=1
        return num==0
    
inputs = "1,#"
s = Solution()
print(s.isValidSerialization(inputs))