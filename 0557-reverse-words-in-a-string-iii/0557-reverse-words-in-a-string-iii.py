class Solution:
    def reverseWords(self, s: str) -> str:
        t=list(s.split())
        r=[i[::-1] for i in t]
        return ' '.join(r)