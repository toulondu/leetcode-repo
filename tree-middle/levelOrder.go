/**
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
**/
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

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int(nil)
	}

	res := [][]int{[]int(nil)}
	cur := []*TreeNode{root}
	curIdx := 0
	// 存储当前行的终点
	end := 0

	for i := 0; i < len(cur); i++ {
		res[curIdx] = append(res[curIdx], cur[i].Val)

		if cur[i].Left != nil {
			cur = append(cur, cur[i].Left)
		}
		if cur[i].Right != nil {
			cur = append(cur, cur[i].Right)
		}

		if i == end && len(cur)-1 > end {
			res = append(res, []int(nil))
			curIdx++
			end = len(cur) - 1
		}
	}

	return res
}

func main() {
	node := TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, &TreeNode{6, nil, nil}, nil}}, &TreeNode{3, nil, &TreeNode{7, nil, nil}}}
	fmt.Println(levelOrder(&node))
}
