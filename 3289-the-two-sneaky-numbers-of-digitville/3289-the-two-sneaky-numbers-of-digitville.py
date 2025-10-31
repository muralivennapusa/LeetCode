class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        r=[]
        for i in sorted(set(nums)):
            if nums.count(i)==2:
                r.append(i)
        return r