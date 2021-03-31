'''
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

 

示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boats-to-save-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import heapq
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 构造一个最大堆和一个最小堆
        res = 0
        maxHq = [0]
        minHq = [0]
        for w in people:
            heapq.heappush(minHq, w)
            heapq.heappush(maxHq, -w)
        # 从最大堆和最小堆中分别取值
        minValue = heapq.heappop(minHq)
        maxValue = -heapq.heappop(maxHq)

        while minValue < maxValue:
            # 如果加起来大于limit，就把小的塞回去
            if(maxValue+minValue > limit):
                heapq.heappush(minHq, minValue)
            res += 1
            minValue = heapq.heappop(minHq)
            maxValue = -heapq.heappop(maxHq)

        print(res, minValue, maxValue, maxHq)
        # 现在剩下一组相同的值
        while minValue == maxValue:
            if maxValue <= limit//2:
                heapq.heappop(maxHq)
            res += 1
            maxValue = -heapq.heappop(maxHq)

        return res


s = Solution()
ans = s.numRescueBoats([1, 2], 3)
print('answer===', ans)
