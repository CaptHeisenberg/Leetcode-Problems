from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # char count
        for s in strs:
            count = [0] * 26  # one count for each letter
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)  # Now correctly placed
        return list(res.values())
