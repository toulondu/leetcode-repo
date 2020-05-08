# -*- encoding: utf-8 -*-
'''
@FILE           :longestSubstring.py
@TIME           :2020/05/06 17:02:11
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

395. 至少有K个重复字符的最长子串

找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 标准DP算法的题，不过有优化空间。
# 不过这里我只做了一个最简单的优化，即用正则进行split把所有出现次数低于k的都作为分割点。
# 理论上还可以继续优化
# 比如先计算一个子串的最大长度n，如果其它子串的长度直接小于n,则没有再计算的必要了。

from collections import Counter
import re

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0
        if k==1: return len(s)
        
        # 用正则把所有次数低于k的字符都作为分割点，尽量减少递归次数
        lower_k_re = '|'.join([c for c,n in Counter(s).items() if n<k])
        if not lower_k_re: return len(s)

        lowers = re.split(lower_k_re,s)
        return max([self.longestSubstring(a,k) for a in lowers])
