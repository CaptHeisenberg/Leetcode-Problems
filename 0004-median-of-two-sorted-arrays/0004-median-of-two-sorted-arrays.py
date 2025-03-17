from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize the binary search.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # If partitionX is 0, use -infinity for maxLeftX.
            # If partitionX is m, use +infinity for minRightX.
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            # Similarly for nums2.
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the correct partition.
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total length is even, median is average of two middle elements.
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move left in nums1.
                high = partitionX - 1
            else:
                # Move right in nums1.
                low = partitionX + 1
        
        # If no partition is found (should not happen if inputs are sorted).
        raise ValueError("Input arrays are not sorted properly")
