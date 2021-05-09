/**
 * 206. 反转链表
 * 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 提示：

	链表中节点的数目范围是 [0, 5000]
	-5000 <= Node.val <= 5000


	进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
*/
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	cur := head
	var res *ListNode = nil

	for cur != nil {
		temp := res
		res = cur
		cur = cur.Next
		res.Next = temp

		// 似乎golang没有如下的多元赋值，res.Next不能正确的赋值，而是会赋值给cur.Next.Next
		// res, res.Next, cur = cur, res, cur.Next
	}
	return res
}

func main() {
	node := ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
	res := reverseList(&node)
	fmt.Println(res.Val, res.Next.Val, res.Next.Next.Val)

	// head := &node
	// fmt.Println(head, head.Next)
	// head.Next, head = head, head.Next
	// fmt.Println(head.Next)
}
