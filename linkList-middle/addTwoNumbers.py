'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        multi = 1
        while l1 is not None:
            n1 += l1.val * multi
            l1 = l1.next
            multi *= 10

        multi = 1
        while l2 is not None:
            n2 += l2.val * multi
            l2 = l2.next
            multi *= 10

        dividedNum = (n1+n2) // 10
        res = ListNode((n1+n2) % 10)
        nxt = res

        while dividedNum > 0:
            nxt.next = ListNode(dividedNum % 10)
            dividedNum = dividedNum//10
            nxt = nxt.next

        return res

# 优化，一次遍历解决
# 计算进位，初始化ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        self.add(l1, l2, 0, res)
        return res.next

    def add(self, l1: ListNode, l2: ListNode, addition, current: ListNode):
        summ = addition
        if l1 is None and l2 is None and addition == 0:
            return
        if l1:
            summ += l1.val
        if l2:
            summ += l2.val

        if summ > 9:
            addition = 1
            summ = summ % 10
        else:
            addition = 0
        current.next = ListNode(summ)
        self.add(l1.next if l1 else l1,
                 l2.next if l2 else l2, addition, current.next)


s = Solution2()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
res = s.addTwoNumbers(l1, l2)
while res is not None:
    print(res.val)
    res = res.next
