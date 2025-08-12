class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r=-1
        a=len(needle)
        for i in range(0,len(haystack)):
            c=haystack[i:i+a]
            if c==needle:
                r=i
                break
        return r