class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=0
        for i in digits:
            x=x*10
            x=x+i
        x+=1
        r=list(map(int,str(x).strip()))
        return r