/**
	剑指 Offer 59 - I. 滑动窗口的最大值
	难度： 困难

	给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

	示例:

	输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
	输出: [3,3,5,5,6,7]
	解释:

		滑动窗口的位置                最大值
	---------------               -----
	[1  3  -1] -3  5  3  6  7       3
	1 [3  -1  -3] 5  3  6  7       3
	1  3 [-1  -3  5] 3  6  7       5
	1  3  -1 [-3  5  3] 6  7       5
	1  3  -1  -3 [5  3  6] 7       6
	1  3  -1  -3  5 [3  6  7]      7


	提示：

	你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
**/

package main

import "fmt"

func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) == 0 || k == 0 {
		return []int{}
	}
	maxQue := []int{}
	res := []int{}

	i := 1 - k
	for j := 0; j < len(nums); j++ {
		// maxQue是一个单调队列，0为最大，且小于nums[j]的值都会被移除
		// 如果maxQue中最大元素恰好是移动窗口的上一个元素，删除之
		if i > 0 && nums[i-1] == maxQue[0] {
			maxQue = maxQue[1:]
		}

		// 这里的 nums[j] > maxQue[len(maxQue)-1]不能是大于等于，否则同一个滑动窗口有两个最大值相同，就会误删
		for len(maxQue) > 0 && nums[j] > maxQue[len(maxQue)-1] {
			maxQue = maxQue[:len(maxQue)-1]
		}
		maxQue = append(maxQue, nums[j])

		if i >= 0 {
			res = append(res, maxQue[0])
		}
		i++
	}

	return res
}

func main() {
	data := []int{-7, -8, 7, 5, 7, 1, 6, 0}
	fmt.Println(maxSlidingWindow(data, 4))
}
