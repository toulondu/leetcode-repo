# -*- encoding: utf-8 -*-
'''
@FILE           :maxRotateFunction.py
@TIME           :2020/05/06 18:11:33
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

396. 旋转函数

给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。

注意:
可以认为 n 的值小于 105。

示例:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # temp_sum计算每一次旋转后的F(k)，n_sum为sum(A)
        temp_sum = n_sum = 0
        lens = len(A)
        # 第一次循环跑出F(0)和sum(A)
        for i,n in enumerate(A):
            n_sum += n
            temp_sum += i*n
        max_sum = temp_sum

        # 每旋转一次，实际上就是相当于数组的除开最后一位的所有元素乘子+1,结果就增加了 sum(A)-A[-1]
        # 然后再把最后一个元素 A[-1]*(数组长度-1) 减去，实际上就是 F(n) = F(n-1) + sum(A) - A[-1]*len
        k = 1
        while k < lens:
            temp_sum += (n_sum - lens*A[-k])
            max_sum = max(temp_sum,max_sum)
            k+=1
        
        return max_sum