class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:return False
        x=int(n**(0.25))
        for i in range(x+4):
            if 4**i==n:
                return True
        return False