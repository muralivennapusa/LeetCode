class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        r=num
        for i in range(len(s)):
            t=s
            if s[i]=='9':
                t=s[:i]+'6'+s[i+1:]
            else:
                t=s[:i]+'9'+s[i+1:]
            r=max(r,int(t))
        return r