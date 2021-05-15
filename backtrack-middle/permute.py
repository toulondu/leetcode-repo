'''
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''
from typing import List


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            temp = []
            cur = [nums[i]]
            for j in range(len(res)):
                arr = res[j]
                for k in range(len(arr)+1):
                    temp.append(arr[0:k]+cur+arr[k:])
            res = temp
        return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nLen = len(nums)

        def back_trade(nums):
            if len(path) == nLen:
                res.append(path[:])
                return

            for i in range(nLen):
                if nums[i] in path:
                    # 已经在path中了，跳过
                    continue
                path.append(nums[i])
                back_trade(nums)
                path.pop()

        back_trade(nums)
        return res


s = Solution()
res = s.permute([1, 2, 3, 4, 5, 6])
print(res, len(res))
