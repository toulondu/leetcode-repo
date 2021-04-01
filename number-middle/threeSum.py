'''
15. 三数之和
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

from collections import Counter
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      numsDict = Counter(nums)
      numsLen = len(nums)
      
      res = []
      resMap = {}

      for i in range(numsLen):
        first = nums[i]
        for j in range(i+1,numsLen):
          second = nums[j]
          need = 0 - first - second
          numsDict[first]-=1
          numsDict[second]-=1
          if need >= second and need in numsDict and numsDict[need]>0:
            key = str(first)+str(second)+str(need)

            if key not in resMap:
              resMap[key] = 1
              res.append([first,second,need])

          numsDict[first]+=1
          numsDict[second]+=1

      return res

s = Solution()
print(s.threeSum([0]))