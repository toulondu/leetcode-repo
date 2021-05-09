'''
448. 找到所有数组中消失的数字
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]
'''

# 不使用额外空间确实很难想到
# 看了一下提示：
# However, the trick really is to not use any additional space than what is already available to use. 
# Sometimes, multiple passes over the input array help find the solution. 
# However, there's an interesting piece of information in this problem that makes it easy to re-use the input array itself for the solution.
# 遂想到O(n)并不是只能遍历一次，先在原数组上操作，然后再遍历一次操作后的数组得到结果应该也是可行的
# 因为数组的长度为数组值范围，所以每个值-1都是合法下标
# 既不破坏值的下标属性，又要能够判断是否出现过，可以使用正负来进行区分
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      # 把对应下标的数字改造为负数
      for i in range(len(nums)):
        nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
      
      res = []
      for i in range(len(nums)):
        if nums[i]>0:
          res.append(i+1)
      return res

s = Solution();
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))