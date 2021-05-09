/**
*
	136. 只出现一次的数字
	给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

	说明：

	你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

	示例 1:

	输入: [2,2,1]
	输出: 1
	示例 2:

	输入: [4,1,2,1,2]
	输出: 4
**/
package main

import "fmt"

// func singleNumber(nums []int) int {
// 	res := 0
// 	count := make(map[int]bool)
// 	for _, num := range nums {
// 		if count[num] {
// 			res -= num
// 		} else {
// 			count[num] = true
// 			res += num
// 		}
// 	}
// 	return res
// }

// 看了评论区，原来这里可以使用异或来解答
// 交换律：a ^ b ^ c <=> a ^ c ^ b
// 任何数于0异或为任何数 0 ^ n => n
// 相同的数异或为0: n ^ n => 0
// var a = [2,3,2,4,4]
// 2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
func singleNumber(nums []int) int {
	// 这里也不需要res:=0，因为默认初始化就是0
	var res int
	for _, num := range nums {
		res = res ^ num
	}
	return res
}

func main() {
	nums := []int{1, 2, 3, 3, 1, 2, 7}
	fmt.Println(singleNumber(nums))
}
