'''
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

0 <= s.length <= 3000
s 仅由数字组成
'''
from typing import List
class Solution:
    # 这题不难，递归找到所有可能的4段分割，将符合条件的列出应该就可以了
    def restoreIpAddresses(self, s: str) -> List[str]:
      ips = []
      ip = [0,0,0,0]
      # sortNo表示当前是在找第几段，currentIdx则是当前从哪个下标开始找
      def findPart(sortNo,currentIdx):
        # 找齐了4段ip地址
        if sortNo==4:
          if currentIdx == len(s):
            # 找到了4段，当前下标等于长度(表示字符串也搜索完了)，就找到了正确ip
            ips.append('.'.join(ip))
          return

        # 搜索完了字符串，但不够4段
        if currentIdx == len(s):
          return

        # 0只能单独存在，特殊处理
        if s[currentIdx]=='0':
          ip[sortNo]='0'
          findPart(sortNo+1, currentIdx+1)
          return

        # 其它正常情况，枚举之
        base = 0
        for idxEnd in range(currentIdx,len(s)):
          base = base*10 + int(s[idxEnd])
          if base < 256:
            ip[sortNo] = str(base)
            findPart(sortNo+1,idxEnd+1)
          else:
            break
        

      findPart(0,0)
      return ips

s = Solution()
print(s.restoreIpAddresses('0000'))