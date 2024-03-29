// 55. 跳跃游戏
// 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

// 数组中的每个元素代表你在该位置可以跳跃的最大长度。

// 判断你是否能够到达最后一个下标。

// 示例 1：

// 输入：nums = [2,3,1,1,4]
// 输出：true
// 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
// 示例 2：

// 输入：nums = [3,2,1,0,4]
// 输出：false
// 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

// 提示：

// 1 <= nums.length <= 3 * 104
// 0 <= nums[i] <= 105
package main

import (
	"fmt"
)

// 想通了其实很简单，从最后开始往前走
// 一开始的终点为数组最后一位
// 如果某个点能够到达最后终点，就把这个点设为终点
// 继续往前看是否有点能够到达终点
func canJump(nums []int) bool {
	cur := 1
	for i := len(nums) - 2; i >= 0; i-- {
		// 可以从这里到达终点
		if nums[i] >= cur {
			cur = 1
		} else {
			cur += 1
		}
	}

	return cur == 1
}

func main() {
	nums := []int{3, 2, 1, 0, 4}
	fmt.Println(canJump(nums))
}
