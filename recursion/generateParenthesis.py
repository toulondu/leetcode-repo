'''
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
通过次数251,729提交次数326,868
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      res = []

      def generateRecursion(current:str,sub:int,leftLeft:int):
        if leftLeft>0:
          generateRecursion(current+"(",sub+1,leftLeft-1)
        else:
          res.append(current+sub*")")
          return
        
        if sub>0:
          generateRecursion(current+")",sub-1,leftLeft)

      generateRecursion("",0,n)

      return res

s = Solution()
print(s.generateParenthesis(8))