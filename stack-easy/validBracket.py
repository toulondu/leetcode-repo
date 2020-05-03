# -*- encoding: utf-8 -*-
'''
@FILE           :validBracket.py
@TIME           :2020/05/02 13:43:37
@AUTHOR         :Toulon Du
@EMAIL          :seaduhe@gmail.com
@DESCRIPTION    :
@VERSION        :1.0
'''

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    brackets_store = []
    brackets = {'[':1,']':-1,'{':2,'}':-2,'(':3,')':-3}
    for c in s:
        if c in brackets:
            if (len(brackets_store)>0) and (brackets[c] + brackets[brackets_store[-1]]==0):
                brackets_store.pop()
            else:
                brackets_store.append(c)
    return len(brackets_store)==0
