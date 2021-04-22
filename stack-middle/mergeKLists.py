'''
23. 合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
整体思路是用一个最小堆来存储当前所有未遍历完的list的起始节点
然后每一次把最小的节点出堆加入到结果中
如果该出堆的节点还有next，就将其压入堆中
'''


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))

        res = ListNode(0)
        head = res

        while h:
            minV = heapq.heappop(h)
            minIdx = minV[1]
            res.next = lists[minIdx]
            res = res.next
            if lists[minIdx].next:
                lists[minIdx] = lists[minIdx].next
                heapq.heappush(h, (lists[minIdx].val, minIdx))

        return head.next


l1 = ListNode(1, ListNode(2, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(9, ListNode(12))))
l3 = ListNode(3, ListNode(6, ListNode(8, ListNode(11, ListNode(18)))))

s = Solution()
ans = s.mergeKLists([l1, l2, l3])

while ans:
    print(ans.val)
    ans = ans.next
