'''
287. 寻找重复数
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3：

输入：nums = [1,1]
输出：1
示例 4：

输入：nums = [1,1,2]
输出：1
 

提示：

2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
 

进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以在不修改数组 nums 的情况下解决这个问题吗？
你可以只用常量级 O(1) 的额外空间解决这个问题吗？
你可以设计一个时间复杂度小于 O(n2) 的解决方案吗？
'''
from typing import List

# 值位于1-n，那么把值当作下标肯定不会越界
# 其次，有重复元素存在意味着通过把值作为新的下标进行游走是必定会有环存在的(至少有两个next指向一个元素)
# 此时就可以使用快慢指针来找环

# 指针每次走2步，慢指针每次走1步。
# 设相遇时快指针走t2步，慢指针走t1步，环长为c。 则相遇时, 快指针比慢指针多走n个环的长度，即 t2 = t1 + nc。

# 又t2 = 2t1 （快指针走的步数是慢指针的两倍） 则 2t1 = t1 + c, t1=c，即慢指针走了c步。

# 设环起点在第k步，显然慢指针再走k步就会到达环的终点，也是环的起点。如果设置一个i指针从起点开始走，则慢指针和i指针会在环起点相碰。
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      slow,fast = nums[0],nums[nums[0]]
      
      while True:
        if slow==fast:
          # 相遇点，在此把fast移速设为1，slow从起点开始走，再次相遇的点就是重复点
          slow = 0
          while nums[slow]!=nums[fast]:
            slow = nums[slow]
            fast = nums[fast]

          return nums[slow]

        slow = nums[slow]
        fast = nums[nums[fast]]

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
      res = 0
      for i in range(len(nums)):
        idx = abs(nums[i])
        if nums[idx]<0:
          res = idx
          break
        nums[idx] = - nums[idx]
      
      for i in range(len(nums)):
        nums[i] = abs(nums[i])

      return res

s = Solution2()
print(s.findDuplicate([2,5,9,6,9,3,8,9,7,1]))