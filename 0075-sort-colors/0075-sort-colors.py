import random

class Solution:
    def sortColors(self, nums):
        
        def randomized_quick_sort(arr, low, high):
            if low < high:
                pivot_index = randomized_partition(arr, low, high)
                randomized_quick_sort(arr, low, pivot_index - 1)
                randomized_quick_sort(arr, pivot_index + 1, high)
        
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def randomized_partition(arr, low, high):
            pivot_index = random.randint(low, high)
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
            return partition(arr, low, high)

        randomized_quick_sort(nums, 0, len(nums) - 1)

# Example Usage:
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)
