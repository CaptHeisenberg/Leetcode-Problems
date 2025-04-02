class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    cur = (nums[i] - nums[j]) * nums[k]
                    if cur>max:
                        max = cur
        return max if max>0 else 0