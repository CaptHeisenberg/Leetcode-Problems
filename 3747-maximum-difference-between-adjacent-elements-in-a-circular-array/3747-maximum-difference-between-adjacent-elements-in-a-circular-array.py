class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxa = abs(nums[0] - nums[-1])
        for i in range(n-1):
            maxa = max(maxa, abs(nums[i] - nums[i+1]))
        return maxa