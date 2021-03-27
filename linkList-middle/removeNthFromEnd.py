'''
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？


示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 维护两个节点，a节点比b节点慢n步，b到最后，a就指向倒数第n


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         a = b = head
#         step = 0
#         while b.next is not None:
#             b = b.next
#             if step < n:
#                 step += 1
#             else:
#                 a = a.next

#         # 根据题目的描述，只有一种情况 step!=n,即要删除的是第一个元素
#         if step != n:
#             head = head.next
#         else:
#             a.next = None if a.next.next is None else a.next.next

#         return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake = ListNode(0, head)
        a = head
        b = fake
        for i in range(n):
            a = a.next

        while a:
            a = a.next
            b = b.next

        b.next = b.next.next
        return fake.next


s = Solution()
# ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll = ListNode(1)

res = s.removeNthFromEnd(ll, 1)
print(res.val)
