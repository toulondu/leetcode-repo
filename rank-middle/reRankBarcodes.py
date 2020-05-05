# -*- encoding: utf-8 -*-
'''
@FILE           :reRankBarcodes.py
@TIME           :2020/05/04 19:55:29
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

 

示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]
示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
 

提示：

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distant-barcodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 思路：先使用collections.Counter 得到出现次数的统计dict，再以出现次数从多到少排序
# 因为题目保证了有解，那么直接从出现次数最多的元素开始，从0位置隔位插值，超出列表长度后
# 再从第一位开始，因为步幅为2，2趟恰好跑完。

import collections
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count_l = dict(collections.Counter(barcodes))
        lens = len(barcodes)
        res_list = [None]*lens

        idx = 0
        for i in sorted(count_l.keys(), key=lambda x: count_l[x],reverse=True):
            while count_l[i]>0:
                res_list[idx]=i
                idx+=2
                if idx>=lens:
                    idx = 1
                count_l[i]-=1

        return res_list