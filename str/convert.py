'''
6. Z 字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        lenS = len(s)
        if numRows == 1:
            return s
        for i in range(numRows):
            if i >= lenS:
                break
            res += s[i]

            if i != 0 and i != numRows-1:
                j = i
                while True:
                    j1 = j+(numRows-i-1) * 2
                    j2 = j1+2*i
                    if j1 < lenS:
                        res += s[j1]
                    if j2 < lenS:
                        res += s[j2]
                    else:
                        break
                    j = j2
            else:
                gap = (numRows-1)*2
                j = i
                while True:
                    j += gap
                    if j < lenS:
                        res += s[j]
                    else:
                        break

        return res


s = Solution()
print(s.convert("A", 2))
