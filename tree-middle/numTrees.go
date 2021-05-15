/**
	96. 不同的二叉搜索树
	给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。



	示例 1：


	输入：n = 3
	输出：5
	示例 2：

	输入：n = 1
	输出：1


	提示：

	1 <= n <= 19
**/

package main

import "fmt"

// idx下标存储以数组第idx大的元素为顶时，能够返回的搜索树种类数
// 多一个下标0方便计算
// 用f代表numTrees算法
// 以第idx大的元素为顶，则其左边一共 idx-1个元素，右边一共n-idx 个元素，那么一共有 f(idx-1)f(n-idx)种排列方式
// 由此可得，f(n)的值即为以每个点为定点的种类之和
// 算法就是 f(n) = f(0)f(n-1)+f(1)f(n-2)+.....+f(n)f(n-n)
// 应该也算是动态规划了
func numTrees(n int) int {
	kinds := make([]int, n+1)
	kinds[0] = 1
	kinds[1] = 1

	for i := 2; i < n+1; i++ {
		kinds[i] = 0
		for j := 0; j <= i-1; j++ {
			kinds[i] += kinds[j] * kinds[i-j-1]
		}
	}

	return kinds[n]
}

func main() {
	fmt.Println(numTrees(5))
}
