# -*- encoding: utf-8 -*-
'''
@FILE           :findClosedNumbers.py
@TIME           :2020/05/05 15:34:27
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。

示例1:

 输入：num = 2（或者0b10）
 输出：[4, 1] 或者（[0b100, 0b1]）
示例2:

 输入：num = 1
 输出：[2, -1]
提示:

num的范围在[1, 2147483647]之间；
如果找不到前一个或者后一个满足条件的正数，那么输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closed-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#PS: 这个题感觉没什么意思，自己使用的方法和代码感觉也比较丑，没想到效果还超过了99%
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        bigger_one = lower_one = bin(num)[2:]

        # 对于找较大值，即是找到二进制中最后一个01，改为10，再把右边所有的0左移
        bigger_one = '0'+bigger_one
        last01 = bigger_one.rfind('01')
        count0 = bigger_one.count('0',last01+1)
        len1 = len(bigger_one) - last01 - 2 - count0
        bigger_one = bigger_one[0:last01]+'10'+ '0'*count0 + '1'*len1

        # 对于找较小值，则是找到二进制中最后一个10，改为01，再把右边所有的1左移
        last10 = lower_one.rfind('10')
        if last10==-1:
            lower_one = '-1'
        else:
            count1 = lower_one.count('1',last10+1)
            len0 = len(lower_one) - last10 - 2 - count1
            lower_one = lower_one[0:last10]+'01'+'1'*count1 + '0'*len0

        return [int(bigger_one,2),int(lower_one,2)]
