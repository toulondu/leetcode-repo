/**
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

					1
				/ \
				2   3
			/ \
			4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。
*/
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	var maxDiameter int
	var dfs func(node *TreeNode) int

	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		} else {
			leftDeep := dfs(node.Left)
			rightDeep := dfs(node.Right)
			if leftDeep+rightDeep > maxDiameter {
				maxDiameter = leftDeep + rightDeep
			}
			return max(leftDeep, rightDeep) + 1
		}
	}
	dfs(root)
	return maxDiameter
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	data := &TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, &TreeNode{6, nil, &TreeNode{7, nil, nil}}, nil}}, &TreeNode{3, nil, nil}}
	fmt.Println(diameterOfBinaryTree(data))
}
