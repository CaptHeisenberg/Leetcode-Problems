class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        usedbits = 0
        maxlength = 0

        for r in range (len(nums)):
            while (usedbits & nums[r]) != 0:
                usedbits ^=nums[l]
                l+=1
            
            usedbits |= nums[r]
            maxlength = max(maxlength, r-l+1)
        return maxlength