from typing import List

# 采用广度优先来解决


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


s = Solution()
print(s.minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))
