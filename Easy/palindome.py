import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        elif x < 10: return True
        x2 = x
        m = int(math.log(x, 10))
        ref = 0
        while x != 0 :
            ref += (x%10)*(10**m)
            x //= 10
            m -= 1
        return x2 == ref

    # def isPalindrome(self, x:int) -> bool:
    #     return str(x) == str(x)[::-1]