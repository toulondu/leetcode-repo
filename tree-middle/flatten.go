// 114. 二叉树展开为链表
// 给你二叉树的根结点 root ，请你将它展开为一个单链表：

// 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
// 展开后的单链表应该与二叉树 先序遍历 顺序相同。

// 示例 1：

// 输入：root = [1,2,5,3,4,null,6]
// 输出：[1,null,2,null,3,null,4,null,5,null,6]
// 示例 2：

// 输入：root = []
// 输出：[]
// 示例 3：

// 输入：root = [0]
// 输出：[0]

// 提示：

// 树中结点数在范围 [0, 2000] 内
// -100 <= Node.val <= 100

// 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
package main

import "fmt"

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 用一个cur变量来存储当前遍历到的节点
// 把节点是否为空的判断放到递归方法的开始位置
// 只有当节点不为空的时候，才将cur向前推进
// 记得把节点的left设置为空
func flatten(root *TreeNode) {
	cur := root
	var flatten_deep func(node *TreeNode)

	flatten_deep = func(node *TreeNode) {
		if node == nil {
			return
		}
		cur = node

		node.Left, node.Right = node.Right, node.Left
		flatten_deep(node.Right)
		cur.Right = node.Left
		flatten_deep(node.Left)
		node.Left = nil
	}

	flatten_deep(cur)
}

func main() {
	var data *TreeNode = &TreeNode{1, &TreeNode{2, &TreeNode{3, nil, nil}, &TreeNode{4, nil, nil}}, &TreeNode{5, nil, &TreeNode{6, nil, nil}}}
	flatten(data)
	for data != nil {
		fmt.Println(data.Val)
		data = data.Right
	}
}
