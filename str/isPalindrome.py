class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        start, end = 0, len(s)-1

        print(start, end)
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True


s = Solution()
print(s.isPalindrome(-101))
