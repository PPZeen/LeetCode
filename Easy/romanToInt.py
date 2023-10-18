class Solution:
    def romanToInt(self, s):
        ch = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        c = 1
        
        ans = 0
        for e in s[::-1]:
            v = ch[e]
            if v >= c: ans += v
            else: ans -= v
            c = v
        return ans