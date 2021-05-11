// 39. 组合总和
// 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

// candidates 中的数字可以无限制重复被选取。

// 说明：

// 所有数字（包括 target）都是正整数。
// 解集不能包含重复的组合。
// 示例 1：

// 输入：candidates = [2,3,6,7], target = 7,
// 所求解集为：
// [
//   [7],
//   [2,2,3]
// ]
// 示例 2：

// 输入：candidates = [2,3,5], target = 8,
// 所求解集为：
// [
//   [2,2,2,2],
//   [2,3,3],
//   [3,5]
// ]

// 提示：

// 1 <= candidates.length <= 30
// 1 <= candidates[i] <= 200
// candidate 中的每个元素都是独一无二的。
// 1 <= target <= 500

package main

import (
	"fmt"
	"sort"
)

// 通过枚举法，对所有可能性进行遍历。
// 枚举的顺序是 一条路走到黑，发现黑之后，退一步，再向前尝试没走过的路。直到所有路都试过。
func combinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	// 回溯遍历
	res := [][]int{}
	length := len(candidates)

	var calcSum func(idx int, curSum int, current []int)

	calcSum = func(idx int, curSum int, current []int) {
		if curSum > target {
			return
		}
		if curSum == target {
			res = append(res, append([]int(nil), current...))
			return
		}
		// 还不到target
		for i := idx; i < length; i++ {
			if curSum+candidates[idx] > target {
				break
			}
			calcSum(i, curSum+candidates[i], append(current, candidates[i]))
		}
	}

	for idx, _ := range candidates {
		calcSum(idx, candidates[idx], []int{candidates[idx]})
	}
	return res
}

func main() {
	candis := []int{2, 3, 5}
	fmt.Println(combinationSum(candis, 8))
}
