class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        return [(m <= candy+extraCandies) for candy in candies]