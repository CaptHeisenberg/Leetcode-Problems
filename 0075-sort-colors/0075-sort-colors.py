class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if nums[j]<nums[min_index]:
                    min_index = j
            nums[i],nums[min_index] = nums[min_index],nums[i]
        print(nums)

