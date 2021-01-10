'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 贪心算法
# 最小堆求解
import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        sCounts = collections.Counter(S)
        if max(sCounts.values()) > (len(S) + 1) // 2:
            return ''

        hq = [(-x[1], x[0]) for x in sCounts.items()]
        heapq.heapify(hq)

        res = ''

        while len(hq) > 1:
            count1, char1 = heapq.heappop(hq)
            count2, char2 = heapq.heappop(hq)
            res += (char1+char2)
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(hq, (count1, char1))
            if count2 < 0:
                heapq.heappush(hq, (count2, char2))

        if(hq):
            res += hq[0][1]

        return res


s = Solution()
print(s.reorganizeString('aaab'))
