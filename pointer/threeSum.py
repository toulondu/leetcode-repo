'''
15. 三数之和 中等
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numsLen = len(nums)
        res = []

        for i in range(numsLen):
            first = nums[i]
            if first > 0:
                break
            if i > 0 and first == nums[i-1]:
                continue

            # 第三个数字从最后一个开始向前
            thirdIdx = numsLen-1
            target = -first

            for j in range(i+1, numsLen):
                second = nums[j]
                if j > i+1 and second == nums[j-1]:
                    continue

                while j < thirdIdx and second + nums[thirdIdx] > target:
                    thirdIdx -= 1
                if j == thirdIdx:
                    break
                if second+nums[thirdIdx] == target:
                    res.append([first, second, nums[thirdIdx]])

        return res
