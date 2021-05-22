/**
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
**/
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	const MaxUint = ^uint(0)
	const MaxInt = int(MaxUint >> 1)
	const MinInt = -MaxInt - 1

	var dfs func(node *TreeNode, min int, max int) bool

	dfs = func(node *TreeNode, min int, max int) bool {
		if node == nil {
			return true
		}
		if node.Val <= min || node.Val >= max {
			return false
		}
		return dfs(node.Left, min, node.Val) && dfs(node.Right, node.Val, max)
	}

	return dfs(root.Left, -MaxInt-1, root.Val) && dfs(root.Right, root.Val, MaxInt)
}

func buildTree(arr []interface{}) *TreeNode {
	tree := &TreeNode{arr[0].(int), nil, nil}
	queue := []*TreeNode{tree}

	i := 1
	for i < len(arr) {
		cur := queue[0]
		if arr[i] != nil {
			cur.Left = &TreeNode{arr[i].(int), nil, nil}
			queue = append(queue, cur.Left)
		}
		i += 1
		if i < len(arr) {
			if arr[i] != nil {
				cur.Right = &TreeNode{arr[i].(int), nil, nil}
				queue = append(queue, cur.Right)
			}
			i += 1
		}
		queue = queue[1:]
	}
	return tree
}

func main() {
	arr := []interface{}{5, 1, 4, nil, nil, 3, 6}
	tree := buildTree(arr)
	fmt.Println(isValidBST(tree))
}
