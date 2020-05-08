# -*- encoding: utf-8 -*-
'''
@FILE           :calculate.py
@TIME           :2020/05/06 19:50:59
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
'''

import math
import re

class Solution:
    def calculate(self, s: str) -> int:
        patt = re.compile(r'\d+|\+|\*|-|/')
        s = patt.findall(s.replace(' ',''))
        first_num,*nums = s[::2]
        opers = s[1::2]
        cache = [int(first_num)]
        
        for n,oper in zip(nums,opers):
            if oper=='*':
                cache[-1]*=int(n)
            elif oper=='/':
                # 第一次提交这里坑了，整除向下取整导致这里负数会出问题- -
                if cache[-1]<0:
                    cache[-1]=abs(cache[-1])//int(n) * (-1)
                else:
                    cache[-1]//=int(n)
            elif oper=='-':
                cache.append(-1*int(n))
            else:
                cache.append(int(n))
        
        return sum(cache)
