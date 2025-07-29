class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        res = [1] * len_
        for i in range(len_):
            x = nums[i]
            res[i] = 1
            j = i - 1
            while j >= 0 and (nums[j] | x) != nums[j]:
                res[j] = i - j + 1
                nums[j] |= x
                j -= 1
        return res
