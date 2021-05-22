/**
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
*/
package main

import (
	"fmt"
	"math"
)

// func coinChange(coins []int, amount int) int {
// 	if amount == 0 {
// 		return 0
// 	}
// 	cache := make(map[int]int)
// 	steps := coins[0:]

// 	for _, c := range coins {
// 		if c < amount {
// 			cache[c] = 1
// 		} else if c == amount {
// 			return 1
// 		}
// 	}

// 	if len(cache) == 0 {
// 		return -1
// 	}

// 	for len(steps) > 0 {
// 		for _, num := range steps {
// 			for _, coin := range coins {
// 				sum := coin + num
// 				if sum == amount {
// 					return cache[num] + 1
// 				}
// 				if cache[sum] == 0 && sum < amount {
// 					cache[sum] = cache[num] + 1
// 					steps = append(steps, sum)
// 				}
// 			}
// 			steps = steps[1:]
// 		}
// 	}
// 	return -1
// }

// 还是得用动态规划
func coinChange(coins []int, amount int) int {
	if amount < 1 && len(coins) < 1 {
		return -1
	}
	memo := make([]int, amount+1)
	for i := 1; i <= amount; i++ {
		memo[i] = math.MaxInt32
		for _, c := range coins {
			if i >= c && memo[i] > memo[i-c]+1 {
				memo[i] = memo[i-c] + 1
			}
		}
	}
	if memo[amount] == math.MaxInt32 {
		return -1
	}
	return memo[amount]
}

func main() {
	data := []int{1}
	fmt.Println(coinChange(data, 0))
}
