/**
739. 每日温度
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
**/
package main

import "fmt"

func dailyTemperatures(temperatures []int) []int {
	lens := len(temperatures)
	if lens == 0 {
		return temperatures
	}
	res := make([]int, lens)
	res[lens-1] = 0

	var getBigger func(idx int, next int) int
	getBigger = func(idx int, next int) int {
		if temperatures[idx] < temperatures[next] {
			return next - idx
		}
		if res[next] == 0 {
			return 0
		} else {
			return getBigger(idx, next+res[next])
		}
	}

	for i := len(temperatures) - 2; i >= 0; i-- {
		res[i] = getBigger(i, i+1)
	}

	return res
}

func main() {
	data := []int{73}
	fmt.Println(dailyTemperatures(data))
}

// 解法2，单调栈
func dailyTemperatures2(T []int) []int {
	output := make([]int, len(T))
	stack := make([]int, 0)
	for i := 0; i < len(T); i++ {
		// 处理栈内比当前元素小的元素
		for len(stack) != 0 {
			top := stack[len(stack)-1]
			if T[top] < T[i] {
				output[top] = i - top
				stack = stack[:len(stack)-1]
			} else {
				break
			}
		}

		// 将本次的元素入栈
		stack = append(stack, i)
	}
	return output
}
