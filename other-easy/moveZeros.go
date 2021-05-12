// 283. 移动零
// 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

// 示例:

// 输入: [0,1,0,3,12]
// 输出: [1,3,12,0,0]
// 说明:

// 必须在原数组上操作，不能拷贝额外的数组。
// 尽量减少操作次数。
package main

import (
	"fmt"
)

// 把0的位置先占了，然后最后补0
func moveZeroes(nums []int) {
	var notZero int
	for _, num := range nums {
		if num != 0 {
			nums[notZero] = num
			notZero++
		}
	}
	for notZero < len(nums) {
		nums[notZero] = 0
		notZero++
	}
}

func main() {
	arr := []int{0, 1, 0, 3, 12}
	moveZeroes(arr)
	fmt.Println(arr)
}
