class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        r=[]
        x=[0]*n
        for i in nums:
            x[i-1]=1
        for i in range(n):
            if x[i]==0:
                r.append(i+1)
        return r
