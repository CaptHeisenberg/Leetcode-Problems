class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currsum = 0
        for n in nums:
            if currsum <0:
                currsum = 0
            currsum += n
            maxsub = max(maxsub, currsum)
        return maxsub