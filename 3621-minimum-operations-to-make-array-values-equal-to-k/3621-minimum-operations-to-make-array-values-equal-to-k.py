class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        for x in nums:
            if x<k:
                return -1
            elif x>k:
                s.add(x)
        return len(s)