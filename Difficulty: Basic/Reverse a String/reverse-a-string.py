class Solution:
    def reverseString(self, s: str) -> str:
        rs = s[len(s)::-1]
        return rs