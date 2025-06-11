class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Make sure k is not bigger than array size

        # Step 1: Reverse the whole array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the rest
        nums[k:] = reversed(nums[k:])
