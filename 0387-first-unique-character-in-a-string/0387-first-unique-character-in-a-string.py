class Solution:
    def firstUniqChar(self, s: str) -> int:
        r=""
        for i in set(s):
            if s.count(i)==1:
                r+=i
        s=list(s.strip())
        return -1 if len(r)==0 else min([s.index(i) for i in r])
