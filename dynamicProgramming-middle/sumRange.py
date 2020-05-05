# -*- encoding: utf-8 -*-
'''
@FILE           :sumRange.py
@TIME           :2020/05/05 16:32:54
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class NumArray:
    
    def __init__(self, nums: List[int]):
        # 存一个0到每个位置的和的list, 如 sum[n]表示num[0:n]的和(不包括num[n])
        self.sums = [0]*(len(nums)+1)
        for i,n in enumerate(nums):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]