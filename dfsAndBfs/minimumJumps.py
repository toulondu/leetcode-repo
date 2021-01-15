'''
https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/
1654. 到家的最少跳跃次数
有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。

跳蚤跳跃的规则如下：

它可以 往前 跳恰好 a 个位置（即往右跳）。
它可以 往后 跳恰好 b 个位置（即往左跳）。
它不能 连续 往后跳 2 次。
它不能跳到任何 forbidden 数组中的位置。
跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。

给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。



示例 1：

输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出：3
解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。
示例 2：

输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
输出：-1
示例 3：

输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
输出：2
解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。


提示：

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
forbidden 中所有位置互不相同。
位置 x 不在 forbidden 中。
'''

from typing import List
import math

# 第一个思路，最终无法解决forbidden数组的问题


class Solution1:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        '''
        假设最终向前跳n次，向后跳m次达到目标
        由 不能向后连续跳2次，可得n>=m
        且 na - mb = x
        那么当a>b时，可得 n<=x/(a-b)
        而当 a<b时，可得 n >= x/(a-b)
        且 m = (a*n-x)/b
        '''

        if a > b:
            limitValue = int(x/(a-b))+1
            for n in range(1, limitValue):
                m = float(a*n - x) / b
                if m % 1 == 0 and m >= 0:
                    return n+int(m)
            return -1
        if a < b:
            n = math.ceil(x/(b-a))
            while True:
                m = float(a*n - x) / b
                if m % 1 == 0 and m >= 0:
                    return n+int(m)
                n += 1

        return -1

    def ifForbidden(self, m: int, n: int, forbidden: List[int]) -> bool:
        # TODO 判断是否在禁止停留数组中 似乎无法判断

        return True


# 换个思路，采用广度优先来解决

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        maxn = 6000
        s = set(forbidden)
        q = [(0, 0, False)]
        while q:
            cur, step, used = q.pop(0)
            if cur == x:
                return step
            if cur+a < maxn and cur+a not in s:
               # 这一步很关键，将已经尝试过的地方加入禁止数组，表达只要走到这个点上，后面无论怎么走都无效，无需再做尝试
                s.add(cur+a)
                q.append((cur+a, step+1, False))
            if not used and cur-b > 0 and cur-b not in s:
                q.append((cur-b, step+1, True))
        return -1
