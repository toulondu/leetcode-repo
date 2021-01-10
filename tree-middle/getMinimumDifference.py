# -*- encoding: utf-8 -*-
'''
@FILE           :getMinimumDifference.py
@TIME           :2020/05/08 18:54:41
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

530. 二叉搜索树的最小绝对差

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minabs=float('inf')
        stack=[]
        temp = root
        last_v = float('inf')
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            p = stack.pop()
            minabs = min(abs(p.val-last_v),minabs)
            last_v = p.val
            
            if p.right: 
                temp=p.right
                # 如果刚好到root，则stack会为空，所以需要continue跳过最后一句判断
                continue
            if not stack: return minabs