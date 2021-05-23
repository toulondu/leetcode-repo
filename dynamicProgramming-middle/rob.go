/**
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
**/

package main

import "fmt"

// 典型动态规划
// 从前往后计算
// res数组的第i的元素表示的是res[0:i]可以偷窃的最大价值
// 由两种状态转换而来，取其最大值即可
// 1.不偷i，那么res[i] = res[i-1]
// 2.偷i，那么 res[i] = res[i-2]+nums[i]
func rob(nums []int) int {
	lens := len(nums)
	if lens == 1 {
		return nums[0]
	}

	res := make([]int, lens)
	res[0] = nums[0]
	res[1] = max(nums[0], nums[1])

	for i := 2; i < lens; i++ {
		res[i] = max(res[i-1], nums[i]+res[i-2])
	}

	return max(res[lens-1], res[lens-2])
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	data := []int{2, 7, 9, 3, 1}
	fmt.Println(rob(data))
}
