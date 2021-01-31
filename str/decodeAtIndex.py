'''
给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：

如果所读的字符是字母，则将该字母写在磁带上。
如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。

 

示例 1：

输入：S = "leet2code3", K = 10
输出："o"
解释：
解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
字符串中的第 10 个字母是 "o"。
示例 2：

输入：S = "ha22", K = 5
输出："h"
解释：
解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
示例 3：

输入：S = "a2345678999999999999999", K = 1
输出："a"
解释：
解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
 

提示：

2 <= S.length <= 100
S 只包含小写字母与数字 2 到 9 。
S 以字母开头。
1 <= K <= 10^9
题目保证 K 小于或等于解码字符串的长度。
解码后的字符串保证少于 2^63 个字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decoded-string-at-index
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution1:
    def decodeAtIndex(self, S: str, K: int) -> str:
      str=''
      for c in S:
        if c.isalpha():
          str+=c
        else:
          str=str*(int(c))
          if len(str)>=K:
            return str[K-1]
      return str[K-1]

# 偷看答案
# 如果我们有一个像 appleappleappleappleappleapple 这样的解码字符串和一个像 K=24 这样的索引，那么如果 K=4，答案是相同的。

# 一般来说，当解码的字符串等于某个长度为 size 的单词重复某些次数（例如 apple 与 size=5 组合重复6次）时，索引 K 的答案与索引 K % size 的答案相同。
class Solution2:
    def decodeAtIndex(self, S: str, K: int) -> str:
      size = 0
      for c in S:
        if c.isdigit():
          size*=int(c)
        else:
          size+=1
        # if size > K:
        #   break
        #  理论上这里只要size大于K就可以停了，不过需要记录index或者S[0:index],即可以通过空间换时间
        
      for c in reversed(S):
        K%=size
        if K==0 and c.isalpha():
          return c
        if c.isdigit():
          size/=int(c)
        else:
          size-=1

s = Solution2()
print(s.decodeAtIndex('cpmxv8ewnfk3xxcilcmm68d2ygc88daomywc3imncfjgtwj8nrxjtwhiem5nzqnicxzo248g52y72v3yujqpvqcssrofd99lkovg',480551547))