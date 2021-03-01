'''
7. 整数反转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1
'''


class Solution:
    def reverse(self, x: int) -> int:
        # 发现python的整除在负数的时候有问题，就都处理成正数来处理了
        BOUND_VALUE = pow(2, 31) - 1 if x > 0 else pow(2, 31)
        res = 0
        y = abs(x)
        while y != 0:
            mod = y % 10
            y //= 10
            if res > BOUND_VALUE/10:
                return 0

            res = res*10 + mod
        return res if x > 0 else -res


s = Solution()
print(s.reverse(123))
