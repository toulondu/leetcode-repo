# -*- encoding: utf-8 -*-
'''
@FILE           :minimumTotal.py
@TIME           :2020/05/05 17:19:37
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 执行用时 :52 ms, 在所有 Python3 提交中击败了61.97%的用户
# 内存消耗 :14 MB, 在所有 Python3 提交中击败了18.18%的用户
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sum_roads=[0]*(len(triangle)+1)
        triangle.reverse()
        for layer in triangle:
            for i,step in enumerate(layer):
                sum_roads[i] = min(sum_roads[i],sum_roads[i+1]) + step
        
        return sum_roads[0]

# 应该是反序导致的速度降低,优化一版
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lens = len(triangle)
        sum_roads=[0]*(lens)
        for i in range(lens):
            sum_roads[i] = triangle[-1][i]

        for j in range(len(triangle-2),-1,-1):
            for k in range(j+1):
                sum_roads[k] = min(sum_roads[k],sum_roads[k+1]) + triangle[j][k]
        
        return sum_roads[0]

# 看了他人解答，再优化，不需要缓存数组，直接在输入数据上进行修改
class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lens = len(triangle)

        for j in range(lens-2,-1,-1):
            for k in range(j+1):
                triangle[j][k] += min(triangle[j+1][k],triangle[j+1][k+1])
        
        return triangle[0][0]