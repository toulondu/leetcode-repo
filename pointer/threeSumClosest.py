'''
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        minDiff = abs(3*(nums[n-1])) + abs(target) + 1
        res = 0

        for firstIdx in range(n):
            first = nums[firstIdx]

            # # 第一个数大于最小差值/3，直接结束循环
            if first*3 - target > minDiff:
                break

            # 等于上一个数，已经算过，直接跳过
            if firstIdx > 0 and first == nums[firstIdx - 1]:
                continue

            # 指向第三个数的指针从最后一位开始
            thridIdx = n - 1
            subs = target - first
            for secondIdx in range(firstIdx+1, n):
                second = nums[secondIdx]

                if secondIdx > firstIdx+1 and second == nums[secondIdx-1]:
                    continue

                if secondIdx >= thridIdx:
                    break

                while secondIdx < thridIdx-1 and subs - second - nums[thridIdx] < 0:
                    thridIdx -= 1

                if abs(subs - second - nums[thridIdx]) < minDiff:
                    minDiff = abs(subs - second - nums[thridIdx])
                    res = first + second + nums[thridIdx]
                if thridIdx+1 < n and abs(subs - second - nums[thridIdx+1]) < minDiff:
                    minDiff = abs(subs - second - nums[thridIdx+1])
                    res = first + second + nums[thridIdx+1]

        return res


s = Solution()
print(s.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
