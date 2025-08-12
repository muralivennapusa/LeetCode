class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r=[-1]
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]==0:
                t=i-r[-1]
                c=max(t,c)
                r.append(i)
        t=n-r[-1]
        c=max(t,c)
        return c-1
