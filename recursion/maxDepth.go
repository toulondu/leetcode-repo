/**
 *104. 二叉树的最大深度
	给定一个二叉树，找出其最大深度。

	二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

	说明: 叶子节点是指没有子节点的节点。

	示例：
	给定二叉树 [3,9,20,null,null,15,7]，

			3
		/ \
		9  20
			/  \
		15   7
	返回它的最大深度 3 。
*/

/**
 * Definition for a binary tree node.
 */
package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	node := TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, &TreeNode{6, nil, nil}, nil}}, &TreeNode{3, nil, &TreeNode{7, nil, nil}}}
	fmt.Println(maxDepth(&node))
}