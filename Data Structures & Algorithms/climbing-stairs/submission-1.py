class Solution:
    def climbStairs(self, n: int) -> int:
        # if n is two, you either climb 1 + 1 or 2
        # if n is 3, you climb, 1 + 1, + 1, or 2 + 1, 1 + 2 which is 3
        # if n is 4, you can climb 1 + 1 + 1 + 1, 2 + 2, 1 + 1 + 2, 2 + 1 + 1, 1 + 2 + 1 - 5
        # n is 5 = all 1s, 2 + 31s, 1 + 2 + 21s, 1 + 1 + 2 + 1, 31s + 2, 2 + 2 + 1, 1+ 1  + 2, 1 + 2 + 1 = 8
        # 5n = 8, 4n = 5, 3n = 3, 2n = 2, n = 1
        arr = []
        arr.append(1)
        arr.append(2)

        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])

        return arr[n-1]