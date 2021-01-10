'''
在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

你需要输出替换之后的句子。

 

示例 1：

输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 2：

输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"
示例 3：

输入：dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
输出："a a a a a a a a bbb baba a"
示例 4：

输入：dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"
示例 5：

输入：dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
输出："it is ab that this solution is ac"

提示：

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] 仅由小写字母组成。
1 <= sentence.length <= 10^6
sentence 仅由小写字母和空格组成。
sentence 中单词的总量在范围 [1, 1000] 内。
sentence 中每个单词的长度在范围 [1, 1000] 内。
sentence 中单词之间由一个空格隔开。
sentence 没有前导或尾随空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/replace-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
import collections
from functools import reduce

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
      rootDic = {}
      res = []

      # collections.defaultDict 在第一次访问不存在的key后，defaultdict将会生成此key，基于我们的默认值又是一个defaultdict，就能很方便地生成前缀树
      Trie = lambda: collections.defaultdict(Trie)
      trie = Trie()
      # 这个END是用来在前缀树中标识词典中单词，从而判断最短前缀
      END = True
      
      for root in dictionary:
        # 这里初始值为trie，所以是相当于执行 dict.__getitem__(trie,root[0],root[1]),达到了trie[word[-1]][word[-2]].........的效果
        # 详细解释见：https://www.cnblogs.com/ManWingloeng/p/12595809.html
        reduce(dict.__getitem__, root, trie)[END] = root
        # 上面这句作用等于
        # for word in dic:
        #   t = trie
        #   for ch in word:
        #       if ch not in t:
        #           t[ch] = {}
        #       t = t[ch]
        #   t['#'] = '#'

      def replace(word):
        cur = trie
        for letter in word:
          if letter not in cur or END in cur: break
          cur = cur[letter]
        return cur.get(END, word)

      return " ".join(map(replace, sentence.split()))

so = Solution()
print(so.replaceWords(dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
