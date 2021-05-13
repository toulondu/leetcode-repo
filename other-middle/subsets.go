// 78. 子集
// 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

// 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

// 示例 1：

// 输入：nums = [1,2,3]
// 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
// 示例 2：

// 输入：nums = [0]
// 输出：[[],[0]]

// 提示：

// 1 <= nums.length <= 10
// -10 <= nums[i] <= 10
// nums 中的所有元素 互不相同

// 很容易想到一种解法
// 从[]开始，每次将nums中取出一个[x]，和已经有的结果合并，且保留原来的结果
package main

import "fmt"

func subsets(nums []int) [][]int {
	res := [][]int{{}}
	for _, num := range nums {
		addon := [][]int{}
		for _, item := range res {
			// 这里需要把item中的值打到一个新切片中
			// 防止go在空间足够时进行append没有切换底层数组
			addon = append(addon, append(append([]int(nil), item...), num))
		}
		res = append(res, addon...)
	}
	return res
}

func main() {
	data := []int{9, 0, 3, 5, 7}
	fmt.Println(subsets((data)))
}
