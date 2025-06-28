class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0] #assumed that maxsub array starts at 0th index
        currsum = 0 #sum of current sub array
        for n in nums:
            if currsum < 0 :
                currsum = 0 #if currsum is less than 0, it's set to zero to avoid 0 in 1st place 
            currsum += n 
            maxsub = max(maxsub, currsum)
        return maxsub


