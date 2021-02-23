'''
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
'''

from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for idx in range(0,len(nums)):
            numDict[nums[idx]] = idx
        for idx in range(0,len(nums)):
            current = numDict.get(target-nums[idx])
            if current is not None and current!=idx:
                return [current,idx]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for idx,num in enumerate(nums):
          if target-num in numDict:
              return [numDict[target-num],idx]
          numDict[num] = idx
s = Solution()
print(s.twoSum([2,5,5,11],10))
            