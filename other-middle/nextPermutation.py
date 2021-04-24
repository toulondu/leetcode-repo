'''
31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 反序遍历
        for i in range(len(nums)-1, 0, -1):
            # 找到第一个后面数字大雨前面数字的位置
            if nums[i] > nums[i-1]:
                # 交换两者位置
                # 这里错了一次，这里需要找到后面大于nums[i-1]的最小数
                j = len(nums)-1
                while nums[i-1] >= nums[j]:
                    j-=1
                temp = nums[i-1]
                nums[i-1] = nums[j]
                nums[j] = temp
                # 再以此为界限，把后面的部分反序
                nums[i:] = nums[i:][::-1]
                return nums

        nums.reverse()
        return nums


s = Solution()
print(s.nextPermutation([2]))
