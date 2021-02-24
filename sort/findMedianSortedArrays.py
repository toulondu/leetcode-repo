'''
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 解1，拼接2个数组，因为已经排好序，所以下标可以累加
        i1 = 0
        i2 = 0
        arr = []
        for num in nums2:
            for i in range(i1, len(nums1)):
                if num < nums1[i]:
                    arr.append(num)
                    i2 += 1
                    break
                else:
                    i1 += 1
                    arr.append(nums1[i])

        for i in range(i2, len(nums2)):
            arr.append(nums2[i])

        for i in range(i1, len(nums1)):
            arr.append(nums1[i])

        lenArr = len(arr)
        if lenArr == 0:
            return 0
        return (arr[(lenArr-1)//2]+arr[lenArr//2])/2


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 解2 >98%
        nums1.extend(nums2)
        nums1.sort()
        lenArr = len(nums1)
        if lenArr == 0:
            return 0
        return (nums1[(lenArr-1)//2]+nums1[lenArr//2])/2


s = Solution1()
print(s.findMedianSortedArrays([], []))
