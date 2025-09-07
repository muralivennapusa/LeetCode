class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1: return [0]
        x=n//2
        r=[]
        for i in range(1,x+1):
            r.append(i)
            r.append(-i)
        if len(r)!=n:
            r.append(0)
        return r