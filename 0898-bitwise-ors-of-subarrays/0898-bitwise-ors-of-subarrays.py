class Solution:
    def subarrayBitwiseORs(self, A) -> int:
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
            