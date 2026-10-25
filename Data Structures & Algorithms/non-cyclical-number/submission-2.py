class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        while cur not in seen:
            seen.add(cur)
            new = 0
            while cur:
                new += (cur % 10) ** 2 
                cur = cur // 10
            cur = new
            if cur == 1:
                return True
        return False