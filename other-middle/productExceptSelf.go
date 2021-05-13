// 238. 除自身以外数组的乘积
// 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

// 示例:

// 输入: [1,2,3,4]
// 输出: [24,12,8,6]

// 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

// 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

// 进阶：
// 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
package main

import "fmt"

// 这句输出数组不被视为额外空间非常重要， 所以加上输入数组，其实我们有两个数组空间可以使用
// 方法就是遍历两次，第一次遍历用输出数组存储数组每个位置左边所有元素的乘积
// 第二次遍历反序，用一个数字存储当前遍历到的位置的右边数字的乘积
// 而当前位置的值就等于其左边数字的乘积*右边数字的乘积
func productExceptSelf(nums []int) []int {
	length := len(nums)
	var res []int = make([]int, length)
	curProduct := 1

	for i, num := range nums {
		res[i] = curProduct
		curProduct *= num
	}
	curProduct = 1
	for i := length - 1; i >= 0; i-- {
		res[i] *= curProduct
		curProduct *= nums[i]
	}

	return res
}

func main() {
	arr := []int{2, 3, 1, 4}
	fmt.Println(productExceptSelf(arr))
}
