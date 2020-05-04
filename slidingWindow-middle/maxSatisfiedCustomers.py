# -*- encoding: utf-8 -*-
'''
@FILE           :maxSatisfiedCustomers.py
@TIME           :2020/05/04 16:36:51
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。 当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但却只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意的数量。
 

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：
书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 

提示：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        sum_with_last_x = sum_real = max_increase = increase_now = 0

        for i,if_grumpy in enumerate(grumpy):
            sum_real += customers[i]*(1-grumpy[i])
            if i < X:
                sum_with_last_x += customers[i]
            if i == X - 1:
                max_increase = increase_now = (sum_with_last_x - sum_real)
            if i >= X:
                idx = i-X
                increase_now = increase_now - customers[idx]*grumpy[idx] + customers[i]*grumpy[i]
                if increase_now > max_increase: max_increase = increase_now

        return sum_real + max_increase

import time

# 简化一下代码，优化合并一些重复的逻辑，把if改为max函数
class Solution2:
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        sum_real = max_increase = increase_now = 0

        for i,if_grumpy in enumerate(grumpy):
            if not grumpy[i]: sum_real+=customers[i]
            else:
                increase_now = increase_now + customers[i]*grumpy[i]
            if i >= X:
                increase_now -= customers[i-X]*grumpy[i-X]

            max_increase = max(max_increase,increase_now)

        return sum_real + max_increase