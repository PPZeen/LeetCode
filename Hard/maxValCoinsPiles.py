class Solution:
    def maxValueOfCoins(self, piles, k):
        l = len(piles)
        p = [[-1] * (k + 1) for i in range(l + 1)]

        def f(i, coins):
            if i == 0: return 0
            if p[i][coins] != -1: return p[i][coins]
            sum = 0
            for c_coins in range(0, min(len(piles[i-1]), coins) + 1):
                if c_coins > 0:
                    sum += piles[i - 1][c_coins - 1]
                p[i][coins] = max(p[i][coins],
                                f(i - 1, coins - c_coins) + sum)
            return p[i][coins]

        return f(l, k)