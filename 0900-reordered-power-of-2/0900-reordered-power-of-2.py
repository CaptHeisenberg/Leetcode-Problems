from math import log2
from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        seen = set()
        for perm in permutations(s):
            if perm[0] == '0':
                continue
            num = int(''.join(perm))
            if num in seen:
                continue
            seen.add(num)
            if num > 0 and (log2(num)).is_integer():
                return True
        return False
