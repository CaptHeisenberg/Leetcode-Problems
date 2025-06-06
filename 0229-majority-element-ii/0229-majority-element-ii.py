class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        thr = len(nums)//3
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num in count:
            if count[num]>thr:
                res.append(num)
        return res
