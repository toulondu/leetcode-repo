# -*- encoding: utf-8 -*-
'''
@FILE           :decodeString.py
@TIME           :2020/05/06 14:00:13
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def decodeString(self, s: str) -> str:
        
        lens = len(s)
        def dfs(s,i):
            m , temp_s= 0,''
            while i < lens:
                c = s[i]
                if c=='[':
                    # 有[出现，后面就肯定还有],所以不会走完循环从而return最后一句
                    i,next_s = dfs(s,i+1)
                    temp_s+=m*next_s
                    m = 0
                    
                elif c.isalpha():
                    temp_s+=c
                elif c.isnumeric():
                    # 第一次错在没处理超过10的数字
                    m = 10*m + int(c)
                else:
                    # 第二次错在对结尾处理不好
                   return i,temp_s
                i+=1
            return temp_s
        return dfs(s,0)
        
        # counter,strs = [],[]
        # i,lens = 0,len(s)
        # res=''

        # while i < lens:
        #     c=s[i]
        #     if c=='[':
        #         pass
        #     elif c==']':
        #         last_s =strs.pop()*counter.pop()
        #         if strs: strs[-1] += last_s
        #         else: res+=last_s
        #     elif c.isalpha():
        #         temp = c
        #         while i+1<lens and s[i+1].isalpha():
        #             i+=1
        #             temp+=s[i]
        #         strs.append(temp)
        #     elif c.isnumeric():
        #         temp_n = c
        #         while i+1<lens and s[i+1].isnumeric():
        #             i+=1
        #             temp_n+=s[i]
        #         counter.append(int(temp_n))
        #     i+=1
        # if strs: res+=strs[-1]
        # return res
        

s = Solution()
inputs= "3[a]2[b4[F]c]"

print(s.decodeString(inputs))