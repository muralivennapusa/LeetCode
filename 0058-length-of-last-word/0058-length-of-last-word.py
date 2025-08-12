class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=list(s.split())
        return len(w[-1])