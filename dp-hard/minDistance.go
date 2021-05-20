/**
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')


提示：

0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
**/
package main

import "fmt"

func minDistance(word1 string, word2 string) int {
	len1 := len(word1)
	len2 := len(word2)
	if len1 == 0 {
		return len2
	}
	if len2 == 0 {
		return len1
	}

	minDistance := make([][]int, len1)
	// minDistance[i][j] 表示要使word1[0:i]和word2[0:j]相等，需要修改的最少次数
	// 可能由三种情况转换来
	// 1.minDistance[i][j-1]，此时需要在word2[j-1]后面加一个word1[i]，故+1
	// 2.minDistance[i-1][j] ,此时需要在word1[i-1]后面加一个word2[j]，故+1
	// 3.minDistance[i-1][j-1]，此时word[i]若等于word[j],则不需要+1，若相等，则需要+1
	for i := range minDistance {
		minDistance[i] = make([]int, len2)
	}

	// 初始化第0行和第0列的数据
	for i := 0; i < len1; i++ {
		if word1[i] == word2[0] {
			minDistance[i][0] = i
		} else if i != 0 {
			minDistance[i][0] = minDistance[i-1][0] + 1
		} else {
			minDistance[i][0] = 1
		}
	}

	for i := 0; i < len2; i++ {
		if word2[i] == word1[0] {
			minDistance[0][i] = i
		} else if i != 0 {
			minDistance[0][i] = minDistance[0][i-1] + 1
		} else {
			minDistance[0][i] = 1
		}
	}

	for i := 1; i < len1; i++ {
		for j := 1; j < len2; j++ {
			if word1[i] != word2[j] {
				minDistance[i][j] = min(minDistance[i-1][j], minDistance[i][j-1], minDistance[i-1][j-1]) + 1
			} else {
				minDistance[i][j] = min(minDistance[i-1][j]+1, minDistance[i][j-1]+1, minDistance[i-1][j-1])
			}
		}
	}

	return minDistance[len1-1][len2-1]
}

func min(a int, b int, c int) int {
	var minNum int
	if a < b {
		minNum = a
	} else {
		minNum = b
	}
	if c < minNum {
		minNum = c
	}
	return minNum
}

func main() {
	word1 := ""
	word2 := ""

	fmt.Println(minDistance(word1, word2))
}
