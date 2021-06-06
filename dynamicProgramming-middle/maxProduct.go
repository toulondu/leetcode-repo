/**
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
**/
package main

import "fmt"

// func maxProduct(nums []int) int {
// 	lens := len(nums)
// 	if lens == 1 {
// 		return nums[0]
// 	}
// 	positive := make([]int, lens+1)
// 	negative := make([]int, lens+1)
// 	positive[0] = 0
// 	negative[0] = 0
// 	max := nums[0]

// 	for i, num := range nums {
// 		positive[i+1], negative[i+1] = minMax(num, num*positive[i], num*negative[i])
// 		if positive[i+1] > max {
// 			max = positive[i+1]
// 		}
// 	}
// 	return max
// }

// func minMax(a int, b int, c int) (int, int) {
// 	min, max := a, a
// 	if b > max {
// 		max = b
// 	}
// 	if b < min {
// 		min = b
// 	}
// 	if c > max {
// 		max = c
// 	}
// 	if c < min {
// 		min = c
// 	}

// 	return max, min
// }

/**
思路： 求最大值，可以看成求被0拆分的各个子数组的最大值。

当一个数组中没有0存在，则分为两种情况：

1.负数为偶数个，则整个数组的各个值相乘为最大值；

2.负数为奇数个，则从左边开始，乘到最后一个负数停止有一个“最大值”，从右边也有一个“最大值”，比较，得出最大值。
**/
func maxProduct(nums []int) int {
	max := nums[0]
	product := 1

	for _, num := range nums {
		product *= num
		if product > max {
			max = product
		}
		if num == 0 {
			product = 1
		}
	}

	product = 1
	for i := len(nums) - 1; i >= 0; i-- {
		product *= nums[i]
		if product > max {
			max = product
		}
		if nums[i] == 0 {
			product = 1
		}
	}

	return max
}

func main() {
	data := []int{-2, -3}
	fmt.Println(maxProduct(data))
}
