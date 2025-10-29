class Solution:
    def smallestNumber(self, n: int) -> int:
        x=bin(n)[2:]
        return int('1'*len(x),2)