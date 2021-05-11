'''
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

# 初次设想：可以化作一个数学问题
# 首先，n最多包含n/2个2
# 那么，全为1为一种策略
# 每次增加一个2，计算策略数，比如1个2的时候，总步数为n-1，选择一步为2，则为从n-1中选择1步的数量
# 以此类推，直到底数小于顶数
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        def choseMFromN(m: int, n: int) -> int:
            return math.factorial(m) // (math.factorial(m-n) * math.factorial(n))

        # 全1的情况
        res = 1
        bottom = n-1
        while bottom >= n-bottom:
            res += choseMFromN(bottom, n-bottom)
            bottom -= 1

        return res


s = Solution()
print(s.climbStairs(1))
