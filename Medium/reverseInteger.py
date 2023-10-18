class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])
        return 0 if x < -2147483648 or x > 2147483647 else x