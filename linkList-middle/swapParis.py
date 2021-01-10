
# -*- encoding: utf-8 -*-
'''
@FILE           :swapParis.py
@TIME           :2020/05/08 19:28:13
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first,last=head,None
        head = ListNode(0)
        head.next = first
        last = head
        
        while first and first.next:
            temp = first.next
            first.next = temp.next
            temp.next = first
            if last: last.next = temp
            last = first
            first = first.next
        return head.next