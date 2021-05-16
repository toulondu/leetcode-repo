'''
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
'''

# 排序要实现O(n log n) 时间复杂度
# 无非就是归并和快排两种思路
# 这里采用归并来实现
# 归并在于一拆一合
# 拆：将一个列表拆成2部分并分别排序
# 合：将两个拍好序的链表合并
# 而拆可以不断拆，直到被拆分成一个元素为止
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

      def cut(start: ListNode,tail: ListNode):
        if not start:
          return start
        if start.next == tail:
          start.next = None
          return start

        # 找出链表中间点，用快慢指针，慢指针最终将指向中点
        slow = fast = start
        while fast!=tail:
          slow = slow.next
          fast = fast.next
          if fast!=tail:
            fast = fast.next
        
        return merge(cut(start,slow),cut(slow,tail))
      
      def merge(l:ListNode, r:ListNode):
        start = ListNode(0)
        cur,left,right = start,l,r
        
        while left and right:
          if left.val <= right.val:
            cur.next = left
            left = left.next
          else:
            cur.next = right
            right = right.next
          cur = cur.next

          cur.next = left if left else right

        return start.next
          
      return cut(head,None)
      
s = Solution()
node = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
ans = s.sortList(node)
while ans:
  print(ans.val)
  ans = ans.next