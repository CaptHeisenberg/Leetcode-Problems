class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_p = 0
        for num in nums:
            or_p |= num
        return or_p * (1<<(len(nums)-1))